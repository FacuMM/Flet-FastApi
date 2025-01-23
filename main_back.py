from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Modelo para los datos de usuario
class User(BaseModel):
    email: str
    password: str

# Función para conectar a la base de datos
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# Ruta para login
@app.post("/login")
async def login(user: User):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = ? AND password = ?", (user.email, user.password))
    row = cur.fetchone()
    conn.close()
    if row:
        return {"message": "Login exitoso"}
    raise HTTPException(status_code=400, detail="Credenciales incorrectas")

# Ruta para registrar usuario
@app.post("/register")
async def register(user: User):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (email, password) VALUES (?, ?)", (user.email, user.password))
        conn.commit()
        return {"message": "Usuario registrado exitosamente"}
    except:
        raise HTTPException(status_code=400, detail="Error al registrar")
    finally:
        conn.close()
