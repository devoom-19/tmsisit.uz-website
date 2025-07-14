from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Workers import crud, schemas, models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/workers",
    tags=["Workers"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.WorkerOut])
def read_workers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_workers(db, skip=skip, limit=limit)


@router.get("/{worker_id}", response_model=schemas.WorkerOut)
def read_worker(worker_id: int, db: Session = Depends(get_db)):
    db_worker = crud.get_worker(db, worker_id)
    if db_worker is None:
        raise HTTPException(status_code=404, detail="Worker not found")
    return db_worker


@router.post("/", response_model=schemas.WorkerOut)
def create_worker(worker: schemas.WorkerCreate, db: Session = Depends(get_db)):
    return crud.create_worker(db, worker)


@router.put("/{worker_id}", response_model=schemas.WorkerOut)
def update_worker(worker_id: int, worker: schemas.WorkerUpdate, db: Session = Depends(get_db)):
    db_worker = crud.update_worker(db, worker_id, worker)
    if db_worker is None:
        raise HTTPException(status_code=404, detail="Worker not found")
    return db_worker


@router.delete("/{worker_id}")
def delete_worker(worker_id: int, db: Session = Depends(get_db)):
    db_worker = crud.delete_worker(db, worker_id)
    if db_worker is None:
        raise HTTPException(status_code=404, detail="Worker not found")
    return {"ok": True}
