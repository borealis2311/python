from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from user.role import RoleEnum

class UserBase(BaseModel):
    username: str
    email: EmailStr
    isActive: bool = True
    role: RoleEnum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/users/")
def create_user(user: UserBase):
    return user    