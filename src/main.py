"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
from models import db, People
from models import db, Planets
from models import db, Favorite_People
from models import db, Favorite_Planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# ------------------------#
# GET requests

@app.route('/user', methods=['GET'])
def user():
    users = User.query.all()
    one_user = list(map(lambda x: x.serialize(), users))
    return jsonify(one_user), 200

@app.route('/people', methods=['GET'])
def allPeople():
    people_query = People.query.all()
    all_people = list(map(lambda x: x.serialize(), people_query))
    return jsonify(all_people), 200

@app.route('/planets', methods=['GET'])
def allPlanets():
    planets_query = Planets.query.all()
    all_planets = list(map(lambda x: x.serialize(), planets_query))
    return jsonify(all_planets), 200

@app.route('/user/favorites', methods=['GET'])
def userFavs():
    favoriteplanets = Favorite_Planets.query.all()
    favoritepeople = Favorite_People.query.all()
    all_favorite_planets = list(map(lambda x: x.serialize(), favoriteplanets))
    all_favorite_people = list(map(lambda x: x.serialize(), favoritepeople))
    return jsonify(all_favorites), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def onePerson(people_id):
    one_person = People.query.get(people_id)
    return jsonify(one_person.serialize()), 200

@app.route('/planets/<int:planets_id>', methods=['GET'])
def onePlanet(planets_id):
    one_planet = Planets.query.get(planets_id)
    return jsonify(one_planet.serialize()), 200

# POST requests

@app.route('/user', methods=['POST'])
def create_user():
    request_body_user = request.get_json()
    new_user = User(email=request_body_user["email"], username=request_body_user["username"], password=request_body_user["password"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(request_body_user), 200

@app.route('/user/favoriteplanets', methods=['POST'])
def addFavPlanets():
    request_body_planets = request.get_json()
    add_planet = Favorite_Planets(user_id=request_body_planets["user_id"], planet_id=request_body_planet["planet_id"])
    db.session.add(add_planet)
    db.session.commit()
    return jsonify(request_body_planet), 200

@app.route('/user/favoritepeople', methods=['POST'])
def addFavPeople():
    request_body_people = request.get_json()
    add_people = Favorite_People(user_id=request_body_planet["user_id"], people_id=request_body_planet["people_id"])
    db.session.add(add_people)
    db.session.commit()
    return jsonify(request_body_planet), 200

@app.route('/favorite/planet/<int:planets_id>', methods=['DELETE'])
def delFavPlanet(id):
    remove_planet = Favorite_Planet.query.filter_by(id=id).first()
    print("This is the planet to delete: ", id)
    db.session.delete(remove_planet)
    db.session.commit()
    return jsonify(remove_planet.serialize()), 200

@app.route('/user/favorites/people/<int:people_id>', methods=['DELETE'])
def delFavPeople():
    remove_people = Favorite_People.query.filter_by(id=id).first()
    print("This is the person to delete: ", id)
    db.session.delete(remove_people)
    db.session.commit()
    return jsonify(remove_character.serialize()), 200




# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
