from datetime import datetime
from typing import Dict
from pydantic import BaseModel

class UsuarioInDB(BaseModel):
    usuarioid: int = 0
    username: str
    contraseña: str
    nombre: str
    apellido: str
    telefono: int
    identificacion: int
    tipo_identificacion: str
    admin: int
    correo: str


database_usuarios = []
generator = {"id":0}
def save_usuario(usuario_in_db: UsuarioInDB):
    generator["id"] = generator["id"] + 1
    usuario_in_db.usuarioid = generator["id"]
    database_usuarios.append(usuario_in_db)
    return usuario_in_db

database_users = Dict[str, UsuarioInDB]

database_usuarios = {
    1001: UsuarioInDB(**{"usuarioid":"1001",
                            "contraseña":"1234",
                            "username": "Maria_Rios",
                            "nombre":"María",
                            "apellido": "Rios",
                            "telefono": 3134569922,
                            "identificacion": "1077245708",
                            "tipo_identificacion": "cedula",
                            "admin": 1,
                            "correo": "mariarios@gmail.com"}),
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

def get_usuario(usuarioid: int):
    if usuarioid in database_usuarios.keys():
        return database_users[usuarioid]
    else:
        return None

def update_usuario(usuario_in_db: UsuarioInDB):
    database_users[usuario_in_db.usuarioid] = usuario_in_db
    return usuario_in_db

