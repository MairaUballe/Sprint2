from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import update
from db.db_connection import get_db, engine, session
from db.usuarios_db import UsuarioInDB, Usuario
from models.usuarios_models import UsuarioIn, UsuarioOut

router = APIRouter()

@router.post("/usuario/auth/")
async def auth_user(usuario_in: UsuarioIn, db: Session = Depends(get_db)):
    usuario_in_db = db.query(UsuarioInDB).get(usuario_in.username)
    if usuario_in_db == None:
        raise HTTPException(status_code=404,
    detail="El usuario no existe")
    if usuario_in_db.contraseña != usuario_in.contraseña:
        raise HTTPException(status_code=403,
    detail="Error de autenticacion")
    return {"Autenticado": True}

@router.get("/usuarios")           # GET /users HTTP/1.1 (lado del cliente) 
async def usuario():
    usuarios = session.query(UsuarioInDB).all()
    return usuarios

@router.post("/usuarios/create_usuario")
async def create_usaurio(usuario: Usuario): 

    username_in_db = session.query(UsuarioInDB).get(usuario.username)
    if username_in_db == None:
        new_usuario = UsuarioInDB(usuarioid = usuario.usuarioid, username = usuario.username, contraseña = usuario.contraseña, nombre = usuario.nombre, apellido = usuario.apellido, telefono = usuario.telefono, identificacion = usuario.identificacion, tipo_identificacion = usuario.tipo_identificacion, admin = usuario.admin, correo = usuario.correo)
        session.add(new_usuario)
        session.commit()
        return "El usuario " + usuario.username + " ha sido creado sactifactoriamente" 
    else:
        return 409, 'El nombre de usuario ' +  usuario.username + ' no se encuentra disponible'

@router.delete("/usuarios/delete_usuario/")
async def delete_usuario(username: str):
    usuario_in_db = session.query(UsuarioInDB).get(username)
    if usuario_in_db != None:
        session.delete(usuario_in_db)
        session.commit()
        return "El usuario " + username + " ha sido eliminado satifactoriamente"
    raise HTTPException(status_code=404, detail="¡El usuario no existe!")
    

@router.put("/usuario/update_usuario")
async def update_usuario(usuario : Usuario):
    usuario_in_db = session.query(UsuarioInDB).get(usuario.username)

    stmt = (update(UsuarioInDB).where(UsuarioInDB.username == usuario.username).values(contraseña = usuario.contraseña, nombre = usuario.nombre, apellido = usuario.apellido, telefono = usuario.telefono, identificacion = usuario.identificacion, tipo_identificacion = usuario.tipo_identificacion, admin = usuario.admin, correo = usuario.correo))
    
    session.execute(stmt)
    session.commit()
    return 'Actualización exitosa'