from fastapi import FastAPI, t Depends, FastAPI
from routers.user_router import router as router_users
from routers.transaction_router import router as router_transactions
from db.usuarios_db import UsuarioInDB, database_usuarios, get_usuarioid
from fastapi import HTTPException
from models.usuarios_models import UsuarioIn
from db.habitaciones_db import HabitacionesInDB, database_habitaciones, get_habitacionid

api = FastAPI()

api.include_router(router_users)
api.include_router(router_transactions)

@api.get("/")           # GET / HTTP/1.1 (lado del cliente) 
async def root():
    return {"message": "Hello FastAPI ES EL PROYECTO OCCUPO :D"}

# -------------------------USUARIOS -------------------------------------
@api.post("/user/auth/")
async def auth_usuario(usuario_in: UsuarioIn):
    
    usuario_in_db =  get_usuarioid(usuario_in.usuarioid)

    if usuario_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    
    if usuario_in_db.contraseña != usuario_in.contraseña:
        return  {"Autenticado": False}

    return  {"Autenticado": True}


@api.get("/usuarios")           # GET /users HTTP/1.1 (lado del cliente) 
async def usuario():
    return {"message": database_usuarios}


@api.post("/usuarios/create_usuario")
async def create_usaurio(usuario : UsuarioInDB):
    database_usuarios[usuario.usuarioid] = usuario
    return usuario
    

@api.delete("/usuarios/delete_usuario/")
async def delete_usuario(usuario : int):
    if usuario in database_usuarios:
        del database_usuarios[usuario]
    return "El usuario " + str(usuario) + " ha sido eliminado satifactoriamente"
    raise HTTPException(status_code=404, detail="¡El usuario no existe!")


@api.put("/usuario/update_usuario")
async def update_usuario(usuario : UsuarioInDB):
    database_usuarios[usuario.usuarioid] = usuario
    return usuario

# -------------------------HABITACIONES -------------------------------------


@api.get("/habitaciones")           # GET /users HTTP/1.1 (lado del cliente) 
async def habitaciones():
    return {"message": database_habitaciones}


@api.post("/usuarios/create_habitacion")
async def create_habitacion(habitacion : HabitacionesInDB):
    database_habitaciones[habitacion.habitacionid] = habitacion
    return habitacion
    

@api.delete("/usuarios/delete_habitacion/")
async def delete_habitacion(habitacion : int):
    if habitacion in database_habitaciones:
        del database_habitaciones[habitacion]
    return "La habitación " + str(habitacion) + " ha sido eliminada satifactoriamente", database_habitaciones
    raise HTTPException(status_code=404, detail="¡El usuario no existe!")


@api.put("/usuario/update_habitacion")
async def update_habitacion(habitacion : HabitacionesInDB):
    database_habitaciones[habitacion.habitacionid] = habitacion
    return habitacion