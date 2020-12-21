from pydantic import BaseModel
from datetime import datetime

class Disponibilidad(BaseModel):
    disponible: bool
    date: datetime

    class Config:
        orm_mode = True
    
def precios(precio):
    rangoA = 80000
    rangoB = 100000
    rangoC = 180000
    intervalo = 0


