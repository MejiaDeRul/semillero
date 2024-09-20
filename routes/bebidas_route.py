from fastapi import APIRouter
from .db import bebidas
from models.bebidas_model import Bebida, UpdateBebida

router_b = APIRouter()

@router_b.get('/bebidas', tags=['Bebida'])
def mostrar_bebidas():
    return {'bebidas': bebidas}

@router_b.get('/bebidas/{id}', tags=['Bebida'])
def mostrar_una_bebida(id: int):
    return {'msg': bebidas[id]}

@router_b.post('/bebidas', tags=['Bebida'])
def crear_bebida(bebida: Bebida):
    bebidas.append(bebida)
    return {'msg': 'Nueva bebida creada'}

@router_b.put('/bebidas', tags=['Bebida'])
def actualizar_bebida(bebida: UpdateBebida):
    bebidas[bebida.id] = bebida.nuevo
    return {'msg': 'Bebida actualizada'}

@router_b.delete('/bebidas', tags=['Bebida'])
def eliminar_bebida(id: int):
    bebidas.pop(id)
    return {'msg': 'Bebida eliminada'}