from sqlalchemy import Column, Integer, String, Boolean
from db.db_connection import Base, engine
from pydantic import BaseModel

class UsuarioInDB(Base):
    __tablename__ = "usuarios"
    username = Column(String, primary_key=True)
    contraseña = Column(String)
    nombre = Column(String)
    apellido = Column(String)
    fecha_nacimiento = Column(String)
    telefono = Column(String)
    identificacion = Column(String)
    tipo_identificacion = Column(String)
    admin = Column(Boolean)
    correo = Column(String)

Base.metadata.create_all(bind=engine)

class Usuario(BaseModel):
    usuarioid: int = 0
    username: str
    contraseña: str
    nombre: str
    apellido: str
    fecha_nacimiento = str
    telefono: str
    identificacion: str
    tipo_identificacion: str
    admin: bool
    correo: str

def __init__(self, usuarioid, username, contraseña, nombre, apellido, telefono, identificacion, tipo_identificacion, admin, correo):
        super().__init__()
        self.usuarioid = usuarioid
        self.username = username
        self.contraseña = contraseña
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.identificacion = identificacion 
        self.tipo_identificacion = tipo_identificacion
        self.admin = admin
        self.correo = correo

       

""" 
from typing import Dict
from pydantic import BaseModel


database_usuarios = []
generator = {"id":0}
def save_usuario(usuario_in_db: UsuarioInDB):
    generator["id"] = generator["id"] + 1
    usuario_in_db.usuarioid = generator["id"]
    database_usuarios.append(usuario_in_db)
    return usuario_in_db

database_usuarios = Dict[str, UsuarioInDB]

database_usuarios = {
    1001: UsuarioInDB(**{   "usuarioid":"1001",
                            "contraseña":"1234",
                            "username": "Maria_Rios",
                            "nombre":"María",
                            "apellido": "Rios",
                            "telefono": 3134569922,
                            "identificacion": "1077245708",
                            "tipo_identificacion": "cedula",
                            "admin": 1,
                            "correo": "mariarios@gmail.com"
                            "contraseña": "abcd"}),
    1002: UsuarioInDB(**{"usuarioid":"1002",
                            "username": "CarlosGo",
                            "contraseña":"abcd",
                            "nombre":"Carlos",
                            "apellido": "Gomez",
                            "telefono": 3056672365,
                            "identificacion": "1144567342",
                            "tipo_identificacion": "cedula",
                            "admin": 0,
                            "correo": "carlosgo@hotmail.com"}),
    1003: UsuarioInDB(**{"usuarioid":"1003",
                            "username": "Martha44",
                            "contraseña":"aeiou",
                            "nombre":"Martha",
                            "apellido": "Fernandez",
                            "telefono": 3235501234,
                            "identificacion": "16243779",
                            "tipo_identificacion": "cedula",
                            "admin": 1,
                            "correo": "marthafer@gmail.com"}),
}

def get_usuarioid(usaurioid: str):
    if usaurioid in database_usuarios.keys():
        return database_usuarios[usaurioid]
    else: 
        return None
 """