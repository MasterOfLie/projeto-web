from flask import redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from peewee import IntegerField, CharField, Model
from database import db

class User(UserMixin, Model):
    id = IntegerField(primary_key=True)
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db
