from fastapi import FastAPI
from fastapi.responses import JSONResponse
from . import crud

app = FastAPI()

@app.post("/users/", response_model=crud.User)
def create_user(name: str):
    user = crud.create_user(name)
    return user

@app.get("/users/{user_id}/", response_model=crud.User)
def get_user(user_id: int):
    user = crud.get_user_by_id(user_id)
    if user is None:
        return JSONResponse(status_code=404, content={"message": "User not found"})
    return user

@app.put("/users/{user_id}/", response_model=crud.User)
def update_user(user_id: int, name: str):
    user = crud.update_user_name(user_id, name)
    if user is None:
        return JSONResponse(status_code=404, content={"message": "User not found"})
    return user

@app.get("/users/search/", response_model=list[crud.User])
def search_users(query: str):
    users = crud.search_users_by_name(query)
    return users
