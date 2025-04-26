from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class cliente(db.model):
    id = db.column(db.Integer,primary_key=True)
    nombre = db.column(db.string(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    
    vehiculos = db.relationship('Vehiculo', backref='cliente', lazy=True)
    
class Usuario(db.model):
    
    id = db.column(db.Integer,primary_key=True)
    username = db.column(db.String(50), unique=True, nullable=False)
    password = db.column(db.string(100), nullable=False)
    rol = db.column(db.string(20), nullable=False)
    
class Vehiculo (db.model):
    id =db.column(db.Integer,primary_key=True)
    marca = db.column(db.string(50), nullable=False)
    modelo = db.column(db.string(50), nullable=False)
    año = db.column(db.Integer,nullable=False)
    cliente_id = db.column(db.integer, db.Foreignkey('cliente.id'), nullable=False)
    
class Taller_Mecanico(db.model):
    id = db.column(db.Integer, primary_key =True)
    nombre = db.column(db.string(100), nullable=False)
    direccion = db.column(db.string(200), nullable=False)
    telefono = db.column(db.string(20))