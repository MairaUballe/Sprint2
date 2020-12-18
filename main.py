from fastapi import FastAPI, Depends, FastAPI
from routers.usuarios_router import router as router_usuarios
from db.usuarios_db import UsuarioInDB
from fastapi import HTTPException
from models.usuarios_models import UsuarioIn
from db.habitaciones_db import HabitacionesInDB

api = FastAPI()

api.include_router(router_usuarios)



@api.get("/")           # GET / HTTP/1.1 (lado del cliente) 
async def root():
    return {"message": "Hello FastAPI ES EL PROYECTO OCCUPO :D"}
'''

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
    return habitacion '''