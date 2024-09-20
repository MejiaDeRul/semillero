from fastapi import FastAPI
from routes.bebidas_route import router_b

app = FastAPI()
app.include_router(router_b)

@app.get('/')
def home():
    return {'msg': 'Hola'}
