from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    haircolor = Column(String)
    eyecolor = Column(String)

    def __repr__(self):
        return '<People %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "haircolor": self.haircolor,
            "eyecolor": self.eyecolor,
            }



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    password = Column(String(16))
    email = Column(String, unique = True)
    firstname = Column(String)
    lastname = Column(String)