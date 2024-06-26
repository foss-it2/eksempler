from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# Pakker som har med POST
from flask import request

# Pakker som har med database å gjøre.
from flask_sqlalchemy import SQLAlchemy
import os
from models import db, Users, Logg
from datetime import datetime



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

# Oppretter databasetabellene (Kommenter ut/slett denne seksjonen når databasen skal fylles med data, ellers blir alt slettet hver gang appen kjøres.)
with app.app_context():
    try:
        db.create_all()
        print(db)
        print("lagde db!")
    except Exception as e:
        print(f"Error creating tables: {e}")


@app.route("/")
def home():
    mine_bilder = ["/static/duck.jpg","/static/bilde2.png"]
    return render_template('index.html',bilder=mine_bilder) # Sender med parameter bilder

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/<name>")   # Hvis du skriver inn webadressen etterfulgt av forwardslash og tekst vil teksten returneres.
def show_project(name):
    return f"Velkommen kjære {name}"


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
            return f"Hurra {user.fornavn}! Du er logget inn!"
        else:
            return f"Hei {epost}, du har skrevet inn galt passord: {passord}."
    else:
        return render_template("login.html")

@app.route("/logg", methods=['GET'])
def alle_innlogginger():
    innlogginger = Logg.query.all()
    return render_template("logg.html", innlogginger=innlogginger)


if __name__ == "__main__":
    app.run(debug=True)    # Debug er True så feilmeldinger og alt mulig rart vil komme opp i nettleseren.