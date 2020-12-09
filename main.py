from fastapi import FastAPI
from db.usuarios_db import database_usuarios
from fastapi import HTTPException
from db.usuarios_db import UsuarioInDB

api = FastAPI()

@api.get("/")           # GET / HTTP/1.1 (lado del cliente) 
async def root():
    return {"message": "Hello FastAPI ES EL PROYECTO OCCUPO :D"}

@api.get("/usuarios")           # GET /users HTTP/1.1 (lado del cliente) 
async def usuario():
    return {"message": database_usuarios}

@api.get("/usuarios/{usuarioid}")           # GET /users HTTP/1.1 (lado del cliente) 
async def get_usuario_by_usuarioid(usuario : int):
    if usuario in database_usuarios:
        return {"message": database_usuarios[usuario]}
    raise HTTPException(status_code=404, detail="¡El usuario no existe!")

@api.post("/usuarios/create")
async def create_usaurio(usuario : UsuarioInDB):
    database_usuarios[usuario.usuarioid] = usuario
    return usuario

@api.delete("/usuarios/delete")
async def delete_usuario(usuario : UsuarioInDB):
    del database_usuarios[usuario.usuarioid]
    return usuario

@api.put("/usuario/update")
async def update_usuario(usuario : UsuarioInDB):
    database_usuario[usuario.usuarioid] = usuario
    return usuario