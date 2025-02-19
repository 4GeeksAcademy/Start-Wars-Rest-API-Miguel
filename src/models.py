from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),unique=False , nullable=False ) 
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    
    def serialize(self):
        return {
            "name": self.name,
            "id": self.id,
            "email": self.email,

            # do not serialize the password, its a security breach
        }
    

class Character(db.Model):
    __tablename__ = 'character'
    name = db.Column(db.String(30),unique=False , nullable=False ) 
    id = db.Column(db.Integer,primary_key=True)
    birth_year = db.Column(db.String(10),unique=False  , nullable=False )
    eye_color = db.Column(db.String(10),unique=False  , nullable=False )
    gender = db.Column(db.String(10),unique=False  , nullable=False )
    hair_color = db.Column(db.String(10),unique=False  , nullable=False )
    height = db.Column(db.Integer,unique=False  , nullable=False )
    homeworld = db.Column(db.String(200),unique=False  , nullable=False )
    mass = db.Column(db.Integer,unique=False  , nullable=False )
    skin_color = db.Column(db.String(30),unique=False  , nullable=False )
    created = db.Column(db.DateTime,unique=False  , nullable=False )
    edited = db.Column(db.DateTime,unique=False  , nullable=False )
    species = db.Column(db.String(200),unique=False  , nullable=False )
    starships = db.Column(db.String(200),unique=False  , nullable=False )
    url = db.Column(db.String(200),unique=False  , nullable=False ) 
    vehicles = db.Column(db.String(200),unique=False  , nullable=False )
    films = db.Column(db.String(200),unique=False  , nullable=False )
    relation_favorite = db.relationship('Favorite_Character' , backref='character')

    def __repr__(self):
        return '<Character %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
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
    name = db.Column(db.String(30),unique=False  , nullable=False ) 
    id = db.Column(db.Integer,primary_key=True)
    climate = db.Column(db.String(10),unique=False  , nullable=False )
    created = db.Column(db.DateTime,unique=False  , nullable=False )
    diameter = db.Column(db.Integer,unique=False  , nullable=False )
    edited = db.Column(db.DateTime,unique=False  , nullable=False )
    films = db.Column(db.String(200),unique=False  , nullable=False )
    gravity = db.Column(db.Integer,unique=False  , nullable=False )
    orbital_period = db.Column(db.Integer,unique=False  , nullable=False )
    population = db.Column(db.Integer,unique=False  , nullable=False )
    residents = db.Column(db.String(200),unique=False  , nullable=False )
    rotation_period = db.Column(db.Integer,unique=False  , nullable=False )
    surface_water = db.Column(db.Integer,unique=False  , nullable=False )
    terrain = db.Column(db.String(20),unique=False  , nullable=False ) 
    url = db.Column(db.String(200),unique=False  , nullable=False )
    relation_favorite = db.relationship('Favorite_Planet' , backref='planet')

    def __repr__(self):
        return '<Planet %r>' % self.name

    
    def serialize(self):
        return {

            "name": self.name,
            "id": self.id,
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
    id = db.Column(db.Integer,primary_key=True)
    id_character = db.Column(db.Integer, db.ForeignKey('character.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Favorite_Character id_user=%r, id_character=%r>' % (self.id_user, self.id_people)
    

    def serialize(self):
        return {

            "id": self.id,
            "id_character": self.id_character,
            "id_user": self.id_user
    
        }

class Favorite_Planet(db.Model):
    __tablename__ = 'favorite_planet'
    id = db.Column(db.Integer,primary_key=True)
    id_character = db.Column(db.Integer, db.ForeignKey('planet.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Favorite_Planet %r>' % self.id
    

    def serialize(self):
        return {
            
            "id": self.id,
            "id_character": self.id_planet,
            "id_user": self.id_user
    
        }
    

    