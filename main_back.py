from fastapi import FastAPI
from backend.routers import users
from backend import *

app = FastAPI()

# Registrar rutas
app.include_router(users.router)

@app.get("/")
def home():
    return {"message": "Bienvenido a la API"}

# Punto de entrada
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
