from jinja2 import Template
from flask import Flask, request, render_template

app = Flask(__name__)


# Ruter
@app.route('/')
def home():
    # Variabler
    variabler = ["hei","på","deg"]
    return render_template('index.html', variabler=variabler)


if __name__ == '__main__':
    app.run(debug=True)
