import pytest
from sqlalchemy.orm import Session
from database import crud, models
from database.database import SessionLocal

@pytest.fixture(scope="module")
def db():
    db = SessionLocal()
    yield db
    db.close()

def test_create_user(db: Session):
    user = crud.create_user(db, name="Test User")
    assert user.name == "Test User"
    assert user.id is not None

def test_get_user_by_id(db: Session):
    user = crud.create_user(db, name="Test User")
    retrieved_user = crud.get_user_by_id(db, user.id)
    assert retrieved_user == user

def test_update_user_name(db: Session):
    user = crud.create_user(db, name="Test User")
    updated_user = crud.update_user_name(db, user.id, "Updated User")
    assert updated_user.name == "Updated User"

def test_search_users_by_name(db: Session):
    user1 = crud.create_user(db, name="Alice")
    user2 = crud.create_user(db, name="Bob")
    user3 = crud.create_user(db, name="Charlie")

    # Test search with query 'al'
    search_results = crud.search_users_by_name(db, query="al")
    assert user1 in search_results
    assert user3 in search_results
    assert user2 not in search_results
