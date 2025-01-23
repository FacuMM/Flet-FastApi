from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from backend.schemas import UserCreate

DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

# Crear tablas
Base.metadata.create_all(bind=engine)

# Funciones de la base de datos
def get_users():
    with SessionLocal() as session:
        return session.query(User).all()

def create_user(user: UserCreate):
    with SessionLocal() as session:
        new_user = User(username=user.username, password=user.password)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
