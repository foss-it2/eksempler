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


class Svg(db.Model):
    __tablename__ = 'svg'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tegning_id = db.Column(db.Integer, nullable=False)
    fasong = db.Column(db.Integer, nullable=False)
    x_gammel = db.Column(db.Float, nullable=False)
    y_gammel = db.Column(db.Float, nullable=False)
    x = db.Column(db.Float, nullable=False)
    y = db.Column(db.Float, nullable=False)
    r = db.Column(db.Float, nullable=False)
    RR = db.Column(db.Integer, nullable=False)
    GG = db.Column(db.Integer, nullable=False)
    BB = db.Column(db.Integer, nullable=False)
    tid = db.Column(db.BigInteger, nullable=False)