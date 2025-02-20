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
from models import db, User , Character , Planet ,Favorite_Planet , Favorite_Character
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

############################################################################################
#################################----METODOS GET SIN ID----##########################################################
@app.route('/users', methods=['GET'])#
def get_user():

    all_users = User.query.all()

    user_info = [user.serialize() for user in all_users]

    return jsonify(user_info), 200

@app.route('/characters', methods = ['GET'])
def get_character():

    all_characters = Character.query.all()

    info_character = [character.serialize() for character in all_characters]

    return jsonify(info_character), 200

@app.route('/planets', methods = ['GET'])
def get_planet():

    all_planets = Planet.query.all()

    info_planet = [character.serialize() for character in all_planets]

    return jsonify(info_planet), 200

@app.route('/favorite_planets', methods = ['GET'])
def get_favorite_planet():

    all_favorite_planets = Favorite_Planet.query.all()

    info_favorite_planet = [fav_planet.serialize() for fav_planet in all_favorite_planets]

    return jsonify(info_favorite_planet), 200

@app.route('/favorite_characters', methods = ['GET'])
def get_favorite_character():

    all_favorite_characters = Favorite_Character.query.all()

    info_favorite_character = [fav_character.serialize() for fav_character in all_favorite_characters]

    return jsonify(info_favorite_character), 200

############################################################################################
#################################----METODOS GET CON ID----##########################################################

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

############################################################################################
#################################----METODOS POST CON ID----##########################################################

@app.route('/user/<int:id_us>/favorite_character/<int:id_char>', methods = ['POST'])
def post_favorite_character(id_us,id_char):

    exist = Favorite_Character.query.filter_by(id_user = id_us,id_character = id_char).first()

    if exist :

        return jsonify({"msg": "este personaje ya existe en los favoritos de characters"}), 400
    
    new_character_favorite = Favorite_Character(id_user = id_us,id_character = id_char)
    db.session.add(new_character_favorite)
    db.session.commit()

    return jsonify({"msg": "Personaje agregado a la tabla de Favorite_character"})


@app.route('/user/<int:id_us>/favorite_planet/<int:id_pla>', methods = ['POST'])
def post_favorite_planet(id_us,id_pla):

    exist = Favorite_Planet.query.filter_by(id_user = id_us,id_planet = id_pla).first()

    if exist :

        return jsonify({"msg": "este personaje ya existe en los favoritos de planets"}), 400
    
    new_planet_favorite = Favorite_Planet(id_user = id_us,id_planet = id_pla)
    db.session.add(new_planet_favorite)
    db.session.commit()

    return jsonify({"msg": "Personaje agregado a la tabla de Favorite_planet"})


############################################################################################
#################################----METODOS DELETE CON ID----##########################################################

@app.route('/user/<int:id_us>/favorite_planet/<int:id_pla>', methods = ['DELETE'])
def delete_favorite_planet(id_us,id_pla):

    exist = Favorite_Planet.query.filter_by(id_user = id_us,id_planet = id_pla).first()

    if exist :
        db.session.delete(exist)
        db.session.commit()
        return jsonify({"msg": "Personaje eliminado de la tabla de Favorite_planet"})

@app.route('/user/<int:id_us>/favorite_character/<int:id_cha>', methods = ['DELETE'])
def delete_favorite_character(id_us,id_cha):

    exist = Favorite_Character.query.filter_by(id_user = id_us,id_character = id_cha).first()

    if exist :
        db.session.delete(exist)
        db.session.commit()
        return jsonify({"msg": "Personaje eliminado de la tabla de Favorite_Character"})

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
