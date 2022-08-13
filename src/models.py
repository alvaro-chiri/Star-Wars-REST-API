from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    username = db.Column(db.String(30), unique=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
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

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    user = db.relationship('User')
    planets_id = db.Column(db.Integer, db.ForeignKey("Planets.id"), nullable=True)
    planets = db.relationship('Planets', lazy=True)
    people_id = db.Column(db.Integer, db.ForeignKey("People.id"), nullable=True)
    people = db.relationship('People', lazy=True)

    def __repr__(self):
        return '<Favorites %r>' % self.name
    
    def serialize(self):
        return {
            "title": self.title,
            "user_id": self.user_id,            
            "planets": self.planets_id,
            "people": self.people_id
        }


