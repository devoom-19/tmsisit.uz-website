from sqlalchemy.orm import Session
from contact import models


def create_contact_request(db: Session, full_name: str, email: str, phone_number: str, user_comment: str, file_path: str):
    db_contact = models.ContactRequest(
        full_name=full_name,
        email=email,
        phone_number=phone_number,
        korrupsiya="Korrupsiyaga qarshi kurash",
        user_comment=user_comment,
        file_path=file_path
    )
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_contacts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ContactRequest).offset(skip).limit(limit).all()

def get_contact_by_id(db: Session, contact_id: int):
    return db.query(models.ContactRequest).filter(models.ContactRequest.id == contact_id).first()

def delete_contact(db: Session, contact_id: int):
    db_contact = db.query(models.ContactRequest).filter(models.ContactRequest.id == contact_id).first()
    if db_contact:
        db.delete(db_contact)
        db.commit()
    return db_contact
