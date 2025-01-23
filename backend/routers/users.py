from fastapi import APIRouter
from backend.schemas import UserCreate, UserResponse
from backend.database import create_user, get_users

router = APIRouter(prefix="/users", tags=["Users"])

# Ruta para obtener usuarios
@router.get("/", response_model=list[UserResponse])
def list_users():
    return get_users()

# Ruta para crear un nuevo usuario
@router.post("/", response_model=UserResponse)
def add_user(user: UserCreate):
    return create_user(user)
