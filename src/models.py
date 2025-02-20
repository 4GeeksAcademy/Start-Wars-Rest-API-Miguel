from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),unique=False , nullable=False ) 
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    relation_favorite_character = db.relationship('Favorite_Character' , backref='user')
    relation_favorite_planet = db.relationship('Favorite_Planet' , backref='user')



    def __repr__(self):
        return '<User %r>' % self.name
    
    def serialize(self):
        return {
            "name": self.name,
            "id_user": self.id_user,
            "email": self.email,

            # do not serialize the password, its a security breach
        }
    

class Character(db.Model):
    __tablename__ = 'character'
    name = db.Column(db.String(30),unique=False , nullable=False ) 
    id_character = db.Column(db.Integer,primary_key=True)
    birth_year = db.Column(db.String(10))
    eye_color = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    hair_color = db.Column(db.String(10))
    height = db.Column(db.Integer)
    homeworld = db.Column(db.String(200))
    mass = db.Column(db.Integer)
    skin_color = db.Column(db.String(30))
    created = db.Column(db.DateTime)
    edited = db.Column(db.DateTime)
    species = db.Column(db.String(200))
    starships = db.Column(db.String(200))
    url = db.Column(db.String(200)) 
    vehicles = db.Column(db.String(200))
    films = db.Column(db.String(200))
    relation_favorite = db.relationship('Favorite_Character' , backref='character')

    def __repr__(self):
        return '<Character %r>' % self.name
    
    def serialize(self):
        return {
            "id_character": self.id_character,
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "homeworld": self.homeworld,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "created": self.created,
            "edited": self.edited,
            "species": self.species,
            "starships": self.starships,
            "url": self.url,
            "vehicles": self.vehicles,
            "films": self.films
    
        }


class Planet(db.Model):
    __tablename__ = 'planet'
    name = db.Column(db.String(30), nullable=False) 
    id_planet = db.Column(db.Integer,primary_key=True)
    climate = db.Column(db.String(10))
    created = db.Column(db.DateTime)
    diameter = db.Column(db.Integer)
    edited = db.Column(db.DateTime)
    films = db.Column(db.String(200))
    gravity = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    population = db.Column(db.Integer)
    residents = db.Column(db.String(200))
    rotation_period = db.Column(db.Integer)
    surface_water = db.Column(db.Integer)
    terrain = db.Column(db.String(20)) 
    url = db.Column(db.String(200))
    relation_favorite = db.relationship('Favorite_Planet' , backref='planet')

    def __repr__(self):
        return '<Planet %r>' % self.name

    
    def serialize(self):
        return {

            "name": self.name,
            "id_planet": self.id_planet,
            "climate": self.climate,
            "created": self.created,
            "diameter": self.diameter,
            "edited": self.edited,
            "films": self.films,
            "gravity": self.gravity,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "residents": self.residents,
            "rotation_period": self.rotation_period,
            "surface_water": self.surface_water,
            "terrain": self.terrain,
            "url": self.url
    
        }

class Favorite_Character(db.Model):
    __tablename__ = 'favorite_character'
    id_fav_char = db.Column(db.Integer,primary_key=True)
    id_character = db.Column(db.Integer, db.ForeignKey('character.id_character'))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'))

    def __repr__(self):
       return '<Favorite_Character %r>' % self.id_fav_char
    

    def serialize(self):
        return {

            "id": self.id_fav_char,
            "id_character": self.id_character,
            "id_user": self.id_user
    
        }

class Favorite_Planet(db.Model):
    __tablename__ = 'favorite_planet'
    id_fav_planet = db.Column(db.Integer,primary_key=True)
    id_planet = db.Column(db.Integer, db.ForeignKey('planet.id_planet'))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'))

    def __repr__(self):
        return '<Favorite_Planet %r>' % self.id_fav_planet
    

    def serialize(self):
        return {
            
            "id": self.id_fav_planet,
            "id_planet": self.id_planet,
            "id_user": self.id_user
    
        }
    

    