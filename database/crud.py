from sqlalchemy.orm import Session
from models.models import User
from .database import SessionLocal

def create_user(name: str):
    db = SessionLocal()
    try:
        db_user = User(name=name)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    finally:
        db.close()

def get_user_by_id(user_id: int):
    db = SessionLocal()
    try:
        return db.query(User).filter(User.id == user_id).first()
    finally:
        db.close()

def update_user_name(user_id: int, new_name: str):
    db = SessionLocal()
    try:
        db_user = db.query(User).filter(User.id == user_id).first()
        db_user.name = new_name
        db.commit()
        db.refresh(db_user)
        return db_user
    finally:
        db.close()

def search_users_by_name(query: str):
    db = SessionLocal()
    try:
        return db.query(User).filter(User.name.ilike(f"%{query}%")).all()
    finally:
        db.close()
