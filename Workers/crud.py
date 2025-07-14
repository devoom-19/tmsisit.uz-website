from sqlalchemy.orm import Session
from Workers import models, schemas


def get_workers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Worker).offset(skip).limit(limit).all()


def get_worker(db: Session, worker_id: int):
    return db.query(models.Worker).filter(models.Worker.id == worker_id).first()


def create_worker(db: Session, worker: schemas.WorkerCreate):
    worker_data = worker.dict()
    if not worker_data.get("avatar"):
        worker_data["avatar"] = "static/default-avatar.png"
    db_worker = models.Worker(**worker.dict())
    db.add(db_worker)
    db.commit()
    db.refresh(db_worker)
    return db_worker


def update_worker(db: Session, worker_id: int, worker: schemas.WorkerUpdate):
    db_worker = db.query(models.Worker).filter(models.Worker.id == worker_id).first()
    if db_worker:
        for key, value in worker.dict(exclude_unset=True).items():
            setattr(db_worker, key, value)
        db.commit()
        db.refresh(db_worker)
    return db_worker


def delete_worker(db: Session, worker_id: int):
    db_worker = db.query(models.Worker).filter(models.Worker.id == worker_id).first()
    if db_worker:
        db.delete(db_worker)
        db.commit()
    return db_worker
