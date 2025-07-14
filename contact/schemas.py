from pydantic import BaseModel, EmailStr
from typing import Optional


class ContactRequestOut(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone_number: str
    korrupsiya: str
    user_comment: Optional[str] = None
    file_path: str

    class Config:
        orm_mode = True
