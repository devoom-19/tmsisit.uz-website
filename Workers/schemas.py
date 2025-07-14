from pydantic import BaseModel, EmailStr
from typing import Optional


class WorkerBase(BaseModel):
    full_name: str
    position: str
    phone_number: Optional[str] = None
    email: Optional[EmailStr] = None
    avatar: str


class WorkerCreate(WorkerBase):
    pass


class WorkerUpdate(WorkerBase):
    pass


class WorkerOut(WorkerBase):
    id: int

    class Config:
        orm_mode = True
