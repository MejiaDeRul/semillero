from pydantic import BaseModel

class Bebida(BaseModel):
    name: str
    precio: int
    cantidad: float

class UpdateBebida(BaseModel):
    id: int
    nuevo: Bebida