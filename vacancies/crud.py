from sqlalchemy.orm import Session
from vacancies import models, schemas


def get_vacancies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vacancy).offset(skip).limit(limit).all()


def get_vacancy(db: Session, vacancy_id: int):
    return db.query(models.Vacancy).filter(models.Vacancy.id == vacancy_id).first()


def create_vacancy(db: Session, vacancy: schemas.VacancyCreate):
    db_vacancy = models.Vacancy(**vacancy.dict())
    db.add(db_vacancy)
    db.commit()
    db.refresh(db_vacancy)
    return db_vacancy

def update_vacancy(db: Session, vacancy_id: int, vacancy: schemas.VacancyUpdate):
    db_vacancy = db.query(models.Vacancy).filter(models.Vacancy.id == vacancy_id).first()
    if db_vacancy:
        for var, value in vacancy.dict(exclude_unset=True).items():
            setattr(db_vacancy, var, value)
        db.commit()
        db.refresh(db_vacancy)
    return db_vacancy

def delete_vacancy(db: Session, vacancy_id: int):
    db_vacancy = db.query(models.Vacancy).filter(models.Vacancy.id == vacancy_id).first()
    if db_vacancy:
        db.delete(db_vacancy)
        db.commit()
    return db_vacancy
