"""
Databasemodeller
"""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    epost = db.Column(db.String(200), nullable=False, unique=True)
    fornavn = db.Column(db.String(200), nullable=False)
    passord = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime(), default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<epost: {self.epost} fornavn: {self.fornavn}>"


class Logg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    epost = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime(), default=datetime.now(timezone.utc))


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Fremmednøkkel som henviser til en bruker
    bruker_id = db.Column(db.Integer, nullable=False)
    tittel = db.Column(db.Text, nullable=False)   # Tittel på post
    tekst = db.Column(db.Text, nullable=False)   # Teksten i posten
    # url til bildet (på nett, eller lokalt i /static mappen)
    bilde_url = db.Column(db.Text)
    date_added = db.Column(db.DateTime(), default=datetime.now(timezone.utc))
