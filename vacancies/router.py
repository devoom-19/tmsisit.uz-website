from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from vacancies import crud, schemas, models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/management/vacancies",
    tags=["Vacancies"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.VacancyOut])
def read_vacancies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_vacancies(db, skip=skip, limit=limit)

@router.get("/{vacancy_id}", response_model=schemas.VacancyOut)
def read_vacancy(vacancy_id: int, db: Session = Depends(get_db)):
    db_vacancy = crud.get_vacancy(db, vacancy_id)
    if db_vacancy is None:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    return db_vacancy

@router.post("/", response_model=schemas.VacancyOut)
def create_vacancy(vacancy: schemas.VacancyCreate, db: Session = Depends(get_db)):
    return crud.create_vacancy(db, vacancy)

@router.put("/{vacancy_id}", response_model=schemas.VacancyOut)
def update_vacancy(vacancy_id: int, vacancy: schemas.VacancyUpdate, db: Session = Depends(get_db)):
    db_vacancy = crud.update_vacancy(db, vacancy_id, vacancy)
    if db_vacancy is None:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    return db_vacancy

@router.delete("/{vacancy_id}")
def delete_vacancy(vacancy_id: int, db: Session = Depends(get_db)):
    db_vacancy = crud.delete_vacancy(db, vacancy_id)
    if db_vacancy is None:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    return {"ok": True}
