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

@app.route('/people', methods=['GET'])
def allPeople():
    people_query = People.query.all()
    all_people = list(map(lambda x: x.serialize(), people_query))
    return jsonify(all_people), 200

@app.route('/people/int:people_id', methods=['GET'])
def onePerson():
    one_person = People.query.get(id)
    return jsonify(one_person), 200

@app.route('/planets', methods=['GET'])
def allPlanets():
    planets_query = Planets.query.all()
    all_planets = list(map(lambda x: x.serialize(), planets_query))
    return jsonify(all_planets), 200

@app.route('/planets/int:planet_id', methods=['GET'])
def onePlanet():
    return None

@app.route('/user', methods=['GET'])
def user():
    users = User.query.all()
    one_user = list(map(lambda x: x.serialize(), users))
    return jsonify(one_user), 200


@app.route('/user/favorites', methods=['GET'])
def userFavs():
    return None

@app.route('/user/favorites/planet/int:planet_id', methods=['POST'])
def addFavPlanets():
    return None

@app.route('/user/favorites/people/int:people_id', methods=['POST'])
def addFavPeople():
    return None

@app.route('/user/favorites/planet/int:planet_id', methods=['DELETE'])
def delFavPlanet():
    return None

@app.route('/user/favorites/people/int:people_id', methods=['DELETE'])
def delFavPeople():
    return None




# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
