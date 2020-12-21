from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import update
from sqlalchemy.sql.expression import desc, asc
from db.db_connection import get_db, engine, session
from db.habitaciones_db import HabitacionesInDB, Habitacion

router = APIRouter()


@router.get("/habitaciones")           # GET /users HTTP/1.1 (lado del cliente) 
async def Habitaciones():
    habitaciones = session.query(HabitacionesInDB).all()
    return habitaciones
 
@router.post("/habitacioness/create_habitaciones")
async def create_habitaciones(habitacion: Habitacion): 
    habitacionid_in_db = session.query(HabitacionesInDB).get(habitacion.habitacionid)
    if habitacionid_in_db == None:
        new_habitaciones = HabitacionesInDB(habitacionid = habitacion.habitacionid, tipo = habitacion.tipo, disponible = habitacion.disponible, precio = habitacion.precio, descripcion = habitacion.descripcion)
        session.add(new_habitaciones)
        session.commit()
        return "La habitación " + str(habitacion.habitacionid) + " ha sido creada sactifactoriamente" 
    else:
        return 409, 'La habitacion ' + str(habitacion.habitacionid) + ' no se encuentra disponible'

@router.delete("/Habitacioness/delete_Habitaciones/")
async def delete_habitaciones(habitacionid: str):
    habitaciones_in_db = session.query(HabitacionesInDB).get(habitacionid)
    if habitaciones_in_db != None:
        session.delete(habitaciones_in_db)
        session.commit()
        return "La Habitación " + str(habitacionid) + " ha sido eliminado satifactoriamente"
    raise HTTPException(status_code=404, detail="¡La Habitaciones no existe!")
    

@router.put("/Habitaciones/update_Habitaciones")
async def update_Habitaciones(habitacion : Habitacion):
    habitaciones_in_db = session.query(HabitacionesInDB).get(habitacion.habitacionid)

    stmt = (update(HabitacionesInDB).where(HabitacionesInDB.habitacionid == habitacion.habitacionid).values(habitacionid = habitacion.habitacionid, tipo = habitacion.tipo, disponible = habitacion.disponible, precio = habitacion.precio, descripcion = habitacion.descripcion))

    session.execute(stmt)
    session.commit()
    return '¡Actualización exitosa!'

@router.get("/habitaciones/search_habitaciones/tipo")
async def search_habitacionesByTipo(tipo: str):
    tipoHabitaciones_in_db = session.query(HabitacionesInDB).filter_by(tipo= tipo).all()
    return tipoHabitaciones_in_db

@router.get("/habitaciones/search_habitaciones/disponibilidad")
async def search_habitacionesByDisponiblidad(disponible: bool):
    tipoHabitaciones_in_db = session.query(HabitacionesInDB).filter_by(disponible = disponible).all()
    if tipoHabitaciones_in_db == []:
        return "No hay habitaciones disponibles"
    else: 
        return tipoHabitaciones_in_db
        

@router.get("/habitaciones/search_habitaciones/precio")
async def search_habitacionesByPrecio(precio: float):
    if precio == 1:
        habitaciones_in_db = session.query(HabitacionesInDB).filter(HabitacionesInDB.precio < 81000).all()
        return habitaciones_in_db
    if precio == 2:
        habitaciones_in_db1 = session.query(HabitacionesInDB).filter(HabitacionesInDB.precio >= 80000).filter(HabitacionesInDB.precio <= 198000).all()
        return habitaciones_in_db1, 
    if precio == 3:
        habitaciones_in_db = session.query(HabitacionesInDB).filter(HabitacionesInDB.precio > 199000).all()
        return habitaciones_in_db


@router.get("/habitaciones/filter_habitaciones/precio")
async def order_habitacionesByprecio(precio: float):
    if precio == 0:
       orderHabitaciones_in_db = session.query(HabitacionesInDB).order_by(desc(HabitacionesInDB.precio)).all()
    if precio == 1:
        orderHabitaciones_in_db = session.query(HabitacionesInDB).order_by(asc(HabitacionesInDB.precio)).all()
    return orderHabitaciones_in_db