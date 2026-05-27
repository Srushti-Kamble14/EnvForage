from fastapi import APIRouter,HTTPException
from pydantic import BaseModel,EmailStr
from passlib.context import CryptContext
from jose import jwt
import os

router=APIRouter()
pwd=CryptContext(schemes=["bcrypt"],deprecated="auto")
SK=os.getenv("SECRET_KEY","nsoc_secret")

class RegData(BaseModel):
    fname:str
    lname:str
    email:EmailStr
    password:str

class LoginData(BaseModel):
    email:EmailStr
    password:str

users_db={}

@router.post("/signup")
def signup(data:RegData):
    if data.email in users_db:
        raise HTTPException(status_code=400,detail="Email already registered")
    if len(data.password)<6:
        raise HTTPException(status_code=400,detail="Password too short")
    users_db[data.email]={
        "fname":data.fname,
        "lname":data.lname,
        "password":pwd.hash(data.password)
    }
    return {"message":"Account created successfully"}

@router.post("/signin")
def signin(data:LoginData):
    usr=users_db.get(data.email)
    if not usr or not pwd.verify(data.password,usr["password"]):
        raise HTTPException(status_code=401,detail="Invalid email or password")
    token=jwt.encode({"email":data.email},SK,algorithm="HS256")
    return {"token":token,"email":data.email}