from datetime import datetime
from pydantic import BaseModel
from typing import Dict

class HabitacionesInDB(BaseModel):
  habitacionid: int = 0
  habitacionnum: str
  tipo: str
  disponible: int
  precio: float
  personas: int
  

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


 