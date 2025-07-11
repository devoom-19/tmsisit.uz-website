from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str | None = None
    last_name: str | None = None

class UserLogin(BaseModel):
    username: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    email: EmailStr
    first_name: str | None
    last_name: str | None

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
