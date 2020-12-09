from datetime import datetime
from pydantic import BaseModel
import datetime

class PagosInDB(BaseModel):
  pagoid: int 
  total: float
  saldo: float
  fechapago: datetime
  usuarios_usuarioid: int 
  usuarios_username: str 
  reservas_reservaid: int
  reservas_reserva: str 


database_pagos = []
generator = {"id":0}
def save_pagos(pagos_in_db: PagosInDB):
    generator["id"] = generator["id"] + 1
    pagos_in_db.pagoid = generator["id"]
    database_pagos.append(pagos_in_db)
    return pagos_in_db
