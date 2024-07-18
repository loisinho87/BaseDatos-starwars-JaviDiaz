import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Float, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favoritos(Base):
    __tablename__ = 'favoritos'
    vehiculo_id = Column(Integer, ForeignKey('vehiculos.id'), primary_key=True)
    personaje_id = Column(Integer, ForeignKey('personajes.id'), primary_key=True)
    planeta_id = Column(Integer, ForeignKey('planetas.id'), primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    # relaciones con las otras tablas
    usuario = relationship('Usuario', back_populates='favoritos')
    vehiculos = relationship('Vehiculos', back_populates='favoritos')
    personajes = relationship('Personajes', back_populates='favoritos')
    planetas = relationship('Planetas', back_populates='favoritos')


    #Un personaje/planeta/vehículo puede estar en la lista de favoritos de múltiples usuarios (favoritos en Personajes, Planetas, Vehiculos).
    #Cada favorito pertenece a una clase específica (personajes, planetas, vehiculos en Favoritos).


class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    username = Column(String(200), nullable=False, unique=True)
    nombre = Column(String(250), nullable=False)
    apellidos = Column(String(250), nullable=False)
    email = Column(String(200), nullable=False, unique=True)
    password = Column(String(80), nullable=False)
    # relación con favoritos. Estamos diciendo que cada Usuario puede tener múltiples Favoritos, y cada Favorito está asociado con un único Usuario
    favoritos = relationship('Favoritos', back_populates='usuario')

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False, unique=True)
    apellidos = Column(String(250), nullable=False)
    genero = Column(Enum('hombre', 'mujer', 'desconocido', name='genero_tipo'))
    nacimiento = Column(Date, nullable=False)
    altura = Column(Integer)
    peso = Column(Integer)
    color_pelo = Column(String(50))
    color_ojos = Column(String(50))
    
    favoritos = relationship('Favoritos', back_populates='personajes')

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False, unique=True)
    temperatura = Column(String(200))
    diametro = Column(Integer)
    gravedad = Column(Integer)
    poblacion = Column(Integer)
    terreno = Column(String(250))
    superficie_agua = Column(Integer)
    descripcion = Column(String(2000))
    # indica que un planeta puede aparecer en múltiples registros de la tabla Favoritos. 
    # Ejemplo desde una perspectiva de base de datos: un mismo planeta puede estar en la lista de favoritos de diferentes usuarios, pero cada usuario verá solo sus propios favoritos.
    favoritos = relationship('Favoritos', back_populates='planetas')

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False, unique=True)
    tipo_vehiculo = Column(String(200))
    fabricante = Column(String(200))
    precio = Column(String(200))
    longitud = Column(Float)
    pilotos = Column(Integer)
    pasajeros = Column(Integer)
    velocidad = Column(Integer)
    capacidad = Column(Integer)
    consumibles = Column(Integer)
    descripcion = Column(String(2000))
    
    favoritos = relationship('Favoritos', back_populates='vehiculos')

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
