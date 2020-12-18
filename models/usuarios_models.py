from pydantic import BaseModel
from datetime import datetime

class UsuarioIn(BaseModel):
    username: str
    contraseña: str

class UsuarioOut(BaseModel):
    reservaid: int
    correo: str
    date: datetime
    precio: int
    pagoid: int

    class Config:
        orm_mode = True
    