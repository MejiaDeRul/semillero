from fastapi import FastAPI
from pydantic import BaseModel

class Bebida(BaseModel):
    name: str
    price: int
    cant: float

class UpdateBebida(BaseModel):
    id: int
    new: Bebida

app = FastAPI()

bebidas = [
    {'name': 'Coca Cola',
     'price': 5000,
     'cant': 1.5},
    {'name': 'Sprite',
     'price': 4000,
     'cant': 2.5}
]

@app.get('/')
def home():
    return {'msg': 'hola'}

@app.get('/bebida', tags=['Bebidas'])
def mostrar_bebidas():
    return {'bebidas': bebidas}