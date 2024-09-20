from fastapi import FastAPI
from pydantic import BaseModel

class Bebida(BaseModel):
    name: str
    precio: int
    cantidad: float

class UpdateBebida(BaseModel):
    id: int
    nuevo: Bebida

app = FastAPI()

bebidas = [
    {
        'name': 'Coca cola',
        'precio': 5000,
        'cantidad': 1.5
    },
    {
        'name': 'Sprite',
        'precio': 4000,
        'cantidad': 2.5
    }
]

@app.get('/')
def home():
    return {'msg': 'Hola'}

@app.get('/bebidas', tags=['Bebida'])
def mostrar_bebidas():
    return {'bebidas': bebidas}

@app.get('/bebidas/{id}', tags=['Bebida'])
def mostrar_una_bebida(id: int):
    return {'msg': bebidas[id]}

@app.post('/bebidas', tags=['Bebida'])
def crear_bebida(bebida: Bebida):
    bebidas.append(bebida)
    return {'msg': 'Nueva bebida creada'}

@app.put('/bebidas', tags=['Bebida'])
def actualizar_bebida(bebida: UpdateBebida):
    bebidas[bebida.id] = bebida.nuevo
    return {'msg': 'Bebida actualizada'}

@app.delete('/bebidas', tags=['Bebida'])
def eliminar_bebida(id: int):
    bebidas.pop(id)
    return {'msg': 'Bebida eliminada'}