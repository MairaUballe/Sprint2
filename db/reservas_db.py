from datetime import datetime
from pydantic import BaseModel

class ReservaInDB(BaseModel):
    reservaid: int = 0
    usuarios_usuarioid: int
    habitaciones_habitacionid: int
    fecha_ingreso: datetime
    fecha_salida: datetime
    pago: int
    reserva: str
    estado: str

database_reserva = []
generator = {"id":0}
def save_reserva(reserva_in_db: ReservaInDB):
    generator["id"] = generator["id"] + 1
    reserva_in_db.reservaid = generator["id"]
    database_reserva.append(reserva_in_db)
    return reserva_in_db
