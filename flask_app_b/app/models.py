"""
Databasemodeller
"""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    epost = db.Column(db.String(200), nullable=False, unique=True)
    fornavn = db.Column(db.String(200), nullable=False)
    passord = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f"<epost: {self.epost} fornavn: {self.fornavn}>"


class Logg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    epost = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime(), default=datetime.utcnow)
