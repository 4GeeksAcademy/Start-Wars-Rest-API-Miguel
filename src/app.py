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
from models import db, User , Character , Planet
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
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

@app.route('/user', methods=['GET'])
def get_user():

    all_users = User.query.all()

    user_info = [user.serialize() for user in all_users]

    return jsonify(user_info), 200

@app.route('/character', methods = ['GET'])
def get_character():
    
    all_characters = Character.query.all()

    info_character = [character.serialize() for character in all_characters]

    return jsonify(info_character), 200

@app.route('/character/<int:id>', methods = ['GET'])
def get_character_id(id):

    character_by_id = Character.query.get(id)

    info_character_by_id = character_by_id.serialize()

    return jsonify(info_character_by_id), 200

@app.route('/planet/<int:id>', methods = ['GET'])
def get_planet_id(id):

    planet_by_id = Planet.query.get(id)

    info_character_by_id = planet_by_id.serialize()

    return jsonify(info_character_by_id), 200

@app.route('/planet', methods = ['GET'])
def get_planet():
    
    all_planets = Planet.query.all()

    info_planet = [character.serialize() for character in all_planets]

    return jsonify(info_planet), 200


# @app.route('/favorite_planet', methods = ['GET'])
# def get_favorite_planet():
    
#     all_favorite_planets = Character.query.all()

#     info_favorite_planet = [character.serialize() for character in all_favorite_planets]

#     return jsonify(info_favorite_planet), 200

@app.route('/favorite_character', methods = ['GET'])
def get_favorite_character():
    
    all_favorite_characters = Character.query.all()

    info_favorite_character = [character.serialize() for character in all_favorite_characters]

    return jsonify(info_favorite_character), 200


# @app.route('/character', methods = ['GET'])
# def get_character():


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
