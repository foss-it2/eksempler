from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__,
    static_folder='static',
    template_folder='templates')
Bootstrap(app)  # Benytter Bootstrap-bibliotek for å benytte Bootstrap funksjonalitet i html-templates.



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return "Returnerer en tekst om oss :)"

@app.route("/<name>")   # Hvis du skriver inn webadressen etterfulgt av forwardslash og tekst vil teksten returneres.
def show_project(name):
    return f"Velkommen {name}"


if __name__ == "__main__":
    app.run(debug=True)    # Debug er True så feilmeldinger og alt mulig rart vil komme opp i nettleseren.