from pydantic import BaseModel
from datetime import datetime

class UsuarioIn(BaseModel):
    usuarioid: int
    contraseña: str

class UsuarioOut(BaseModel):
    reservaid: int
    correo: str
    date: datetime
    precio: int
    pagoid: int
    