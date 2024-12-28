from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# Pakker som har med POST
from flask import request

# Pakker som har med database å gjøre.
import os
from models import db, Users, Logg, Posts
from datetime import datetime
import pytz # convert from UTC to local time

# Pakker som har med innlogging å gjøre
from flask import session

# Pakker som har med socket.io å gjøre
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
from threading import Lock



app = Flask(__name__,
    static_folder='static',
    template_folder='templates')
Bootstrap(app)  # Benytter Bootstrap-bibliotek for å benytte Bootstrap funksjonalitet i html-templates.

# Legg til database
database_path = os.path.join(app.root_path, "database.db")
app.config["SECRET_KEY"] = "superhemmelignøkkel"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + database_path
print(app.config['SQLALCHEMY_DATABASE_URI'])

# Starter databasen ved å koble appen til databasen.
# Initialize the db object
db.init_app(app)

# Oppretter databasetabellene (Overskriver ikke hvis databasefilen database.db allerede er opprettet.)
with app.app_context():
    try:
        db.create_all()
        print(db)
        print("Created db tables")
    except Exception as e:
        print(f"Error creating tables: {e}")

# Initializes socket.io
# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

# Kode for å slette en rad i tabellen Posts (eller bytte it Posts med en annen tabell).
# with app.app_context():
#     row_to_delete = Posts.query.filter_by(id=2).first()

# # Check if the row exists before attempting to delete
# if row_to_delete:
#     with app.app_context():
#         db.session.delete(row_to_delete)
#         db.session.commit()

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        print("Sending server generated event")
        socketio.emit('my_response', {'data': 'Server generated event', 'count': count})



@app.route("/")
def home():
    mine_bilder = ["/static/duck.jpg","/static/bilde2.png"]
    return render_template('index.html',bilder=mine_bilder) # Sender med parameter bilder

@app.route("/about")
def about():
    return render_template('about.html')



# Databasehåndtering

@app.route("/add", methods=['GET', 'POST'])
def add_user():
    if request.method == "POST":
        data = request.form
        ny_epost = data["epost"]
        nytt_fornavn = data["fornavn"]
        nytt_passord = data["passord"]
        print(nytt_fornavn, ny_epost, nytt_passord)
        # Sjekker om bruker allerede finnes med den epostadressen:
        with app.app_context():
            user = Users.query.filter_by(epost=ny_epost).first()  # Finner alle brukere med den epostadressen og returnerer den første.
        # Hvis bruker ikke finnes, legg den til databasen:
        if user == None:
            user = Users(epost=ny_epost, fornavn=nytt_fornavn, passord=nytt_passord)
            db.session.add(user)
            db.session.commit()
            return f"Hei {nytt_fornavn}. Du er lagt til i databasen med unik epost: {ny_epost}"
        else:
            return f"Hei {user.fornavn}! Du har allerede lagt deg inn i databasen på tidspunkt {user.date_added}."
    else:
        return render_template("legg_til_bruker.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        data = request.form
        epost = data["epost"]
        passord = data["passord"]
        # Sjekker om brukernavn og passord matcher databasen.
        user = Users.query.filter_by(epost=epost).first()
        if user.passord == passord:
            # Loggføring.
            post = Logg(epost=epost)
            db.session.add(post)
            db.session.commit()
            # Setter en session-variabel til innlogget.
            session["current_user"] = user.epost
            return render_template("hemmelig_side.html", epost=session["current_user"])
        else:
            return f"Hei {epost}, du har skrevet inn galt passord: {passord}."
    else:
        return render_template("login.html")

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.clear()
    return "Du er logget ut."

@app.route("/logg", methods=['GET'])
def alle_innlogginger():
    innlogginger = Logg.query.all()
    for logg in innlogginger:
        print(logg.id,logg.epost,logg.date_added)
    return render_template("logg.html", innlogginger=innlogginger)


@app.route("/brukere", methods=['GET'])
def alle_brukere():
    brukere = Users.query.all()
    return render_template("brukere.html", brukere=brukere)


@app.route("/posts", methods=['GET'])
def alle_posts():
    print("sjekker db")
    posts = Posts.query.all()
    print("Ferdgi sjekke db")
    posts = Posts.query.all()
    local_tz = pytz.timezone('Europe/Oslo')  # Replace with your local timezone
    for post in posts:
        post.date_added = post.date_added.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return render_template("posts.html", posts=posts)


@app.route("/add_post", methods=['GET', 'POST'])
def add_post():
    if request.method == "POST":
        data = request.form
        tittel = data["tittel"]
        tekst = data["tekst"]
        bruker_id = data["bruker_id"]
        bilde_url = data["bilde_url"]
        print(bruker_id, tittel, tekst)
        # Sjekker om bruker allerede finnes med den epostadressen:
        with app.app_context():
            # Legger inn posten i databasen
            post = Posts(bruker_id=bruker_id, tittel=tittel, tekst=tekst, bilde_url=bilde_url)
            db.session.add(post)    # Legger data inn i databasen.
            db.session.commit()     # Bekrefter at databasen skal lagre.
            # Henter alle posts som kan sendes tilbake til nettsiden:
            alle_posts = Posts.query.all()
            return render_template("posts.html", posts=alle_posts)
    else:
        return render_template("legg_til_post.html")


@socketio.event
def my_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']})


@socketio.event
def my_broadcast_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)


@socketio.event
def join(message):
    join_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})


@socketio.event
def leave(message):
    leave_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})


@socketio.on('close_room')
def on_close_room(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response', {'data': 'Room ' + message['room'] + ' is closing.',
                         'count': session['receive_count']},
         to=message['room'])
    close_room(message['room'])


@socketio.event
def my_room_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']},
         to=message['room'])


@socketio.event
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()

    session['receive_count'] = session.get('receive_count', 0) + 1
    # for this emit we use a callback function
    # when the callback function is invoked we know that the message has been
    # received and it is safe to disconnect
    emit('my_response',
         {'data': 'Disconnected!', 'count': session['receive_count']},
         callback=can_disconnect)


@socketio.event
def my_ping():
    emit('my_pong')

clients = []

@socketio.event
def client_info(data):
    client_id = data['clientId']
    platform = data['platform']
    user_agent = data['userAgent']
    print(f"Client connected: {client_id}")
    print(f"Platform: {platform}, User Agent: {user_agent}")
    # Store or manage client information as needed
    if client_id not in clients:
        clients.append(client_id)
    else:
        print("Client already in list")


@socketio.event
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected', request.sid)


@socketio.event
def my_click_event(message):
    print("Received click event: ", message)


@socketio.event
def client_timer_event(message):
    id = -1
    if message["client_id"] in clients:
        id=clients.index(message["client_id"])
    print(f"Timer event, client: {id}: {message['data']}")


if __name__ == "__main__":
    # Debug er True så feilmeldinger og alt mulig rart vil komme opp i nettleseren.
    app.run(host='0.0.0.0', port=5000, debug=True, )
