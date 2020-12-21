from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, BigInteger, Boolean, Float
from db.db_connection import Base, engine
from xmlrpc.client import boolean
from pydantic import BaseModel

class HabitacionesInDB(Base):
    __tablename__ = "habitaciones"
    habitacionid = Column(BigInteger, primary_key=True)
    tipo = Column(String)
    disponible = Column(Boolean)
    precio = Column(Float)
    descripcion = Column(String)

Base.metadata.create_all(bind=engine)

class Habitacion(BaseModel):
  habitacionid: int = 0
  descripcion: str
  tipo: str
  disponible: bool
  precio: float
  
def __init__(self, habitacionid, descripcion, tipo, disponible, precio):
        super().__init__()
        self.habitacionid = habitacionid
        self.descripcion = descripcion
        self.tipo = tipo
        self.disponible = disponible
        self.precio = precio


""" from datetime import datetime
from pydantic import BaseModel
from typing import Dict

  

database_habitaciones = []
generator = {"id":0}
def save_habitaciones(habitaciones_in_db: HabitacionesInDB):
    generator["id"] = generator["id"] + 1
    habitaciones_in_db.habitacionid = generator["id"]
    database_habitaciones.append(habitaciones_in_db)
    return habitaciones_in_db

database_habitaciones = Dict[str, HabitacionesInDB]

database_habitaciones = {
    101: HabitacionesInDB(**{"habitacionid":101,
                            "habitacionnum":"A101",
                            "tipo": "Sencilla",
                            "disponible": 0,
                            "precio": 100000,
                            "personas": 1,}),
    102: HabitacionesInDB(**{"habitacionid":102,
                            "habitacionnum":"B102",
                            "tipo": "Doble",
                            "disponible":1,
                            "precio": 150000,
                            "personas": 2,}),
    103: HabitacionesInDB(**{"habitacionid":103,
                            "habitacionnum":"C103",
                            "tipo": "Multiple",
                            "disponible": 1,
                            "precio": 200000,
                            "personas": 4,}),
}

def get_habitacionid(habitacionid: int):
    if habitacionid in database_usuarios.keys():
        return database_usuarios[habitacionid]
    else: 
        return None


  """