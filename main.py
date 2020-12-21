from fastapi import FastAPI, Depends, FastAPI
from routers.usuarios_router import router as router_usuarios
from routers.habitaciones_router import router as router_habitaciones
from db.usuarios_db import UsuarioInDB
from fastapi import HTTPException
from models.usuarios_models import UsuarioIn
from db.habitaciones_db import HabitacionesInDB

api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080", "http://localhost:8081, https://test-sprint2.herokuapp.com/",
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

api.include_router(router_usuarios)
api.include_router(router_habitaciones)


@api.get("/")           # GET / HTTP/1.1 (lado del cliente) 
async def root():
    return {"message": "Hello FastAPI ES EL PROYECTO OCCUPO :D"}
