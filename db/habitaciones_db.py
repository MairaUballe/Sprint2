from datetime import datetime
from pydantic import BaseModel
import datetime

class HabitacionesInDB(BaseModel):
  habitacionid: int 
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

 