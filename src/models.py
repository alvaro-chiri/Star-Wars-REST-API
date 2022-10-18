import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# tags = db.Table('tags',
#     db.Column('User_id', db.Integer, db.ForeignKey('User.id'), primary_key=True),
#     db.Column('People_id', db.Integer, db.ForeignKey('People.id'), primary_key=True)
# )

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(30), unique=True)
    # tags = db.relationship('People', secondary=tags, lazy="subquery", backref=db.backref('users', lazy=True))
    people_favorites = db.relationship('People', backref='User', lazy=True)
    planets_favorites = db.relationship('Planets', backref='User', lazy=True)
    # planets_favorites = db.relationship('Favorite_Planets', backref='User', lazy=True)


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            # "favorite_people": list(map(lambda x: x.serialize(), self.favorite_people)),
            # "favorite_planet": list(map(lambda x: x.serialize(), self.favorite_planet))
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    __tablename__ = 'People'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    haircolor = db.Column(db.String(30))
    eyecolor = db.Column(db.String(30))
    gender = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    # people_favorite = db.relationship('Favorite_People', backref='People', lazy=True)


    def __repr__(self):
        return '<People %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "haircolor": self.haircolor,
            "eyecolor": self.eyecolor,
            "gender": self.gender
            }

class Planets(db.Model):
    __tablename__ = 'Planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    diameter = db.Column(db.String(30))
    gravity = db.Column(db.String(30))
    terrain = db.Column(db.String(30))
    climate = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('User_id'))
    # planets_favorite = db.relationship('Favorite_Planets', backref='Planets', lazy=True)

    def __repr__(self):
        return '<Planets %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "climate": self.climate
            }

# class Favorite_People(db.Model):
#     __tablename__ = 'Favorite_People'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
#     people_id = db.Column(db.Integer, db.ForeignKey("People.id"), nullable=True)

#     def __repr__(self):
#         return '<Favorite_People %r>' % self.user_id
    
#     def serialize(self):
#         user = User.query.get(self.user_id)
#         return {
#             "id": self.id,
#             "user": user.username,
#             "people_id": self.people_id
#         }

# class Favorite_Planets(db.Model):
#     __tablename__ = 'Favorite_Planets'
#     id = db.Column(db.Integer, primary_key=True)
#     # user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#     # planets_id = db.Column(db.Integer, db.ForeignKey("Planets.id"), nullable=True)

#     def __repr__(self):
#         return '<Favorite_Planets %r>' % self.user_id
    
#     def serialize(self):
#         user = User.query.get(self.user_id)
#         return {
#             "id": self.id,
#             "user": user.username,
#             "planets_id": self.planets_id
#         }

