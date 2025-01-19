from pydantic import BaseModel
from fastapi import FastAPI, APIRouter, HTTPException

app = FastAPI()
router = APIRouter()

# Dictionary to store user data
users = {}

# Pydantic model for user data
class User(BaseModel):
    name: str
    email: str


# POST request
@router.post("/users/")
async def create_user(user: User):
    if user.name in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user.email] = user.name
    return {"message": "User created successfully"}


# GET request
@router.get("/users/")
async def read_user():
    return users


app.include_router(router)
