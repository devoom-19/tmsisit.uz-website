from pydantic import BaseModel
from datetime import date
from typing import Optional


class VacancyBase(BaseModel):
    title: str
    description: str
    deadline: Optional[date] = None
    phone_number: Optional[str] = None
    location: Optional[str] = None


class VacancyCreate(VacancyBase):
    pass


class VacancyUpdate(VacancyBase):
    pass


class VacancyOut(VacancyBase):
    id: int

    class Config:
        orm_mode = True
