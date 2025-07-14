from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from contact import crud, schemas
from database import SessionLocal
import shutil
import os

router = APIRouter(
    prefix="/contact_user",
    tags=["Contact_user"]
)


# DB sessiya
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# uploads papkani yaratib qo'yamiz
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# faqat rasm fayllarga ruxsat
ALLOWED_TYPES = ["image/jpeg", "image/png", "image/jpg"]


# ---------------------------
# CREATE
@router.post("/", response_model=schemas.ContactRequestOut)
async def create_contact_request(
    full_name: str = Form(...),
    email: str = Form(...),
    phone_number: str = Form(...),
    user_comment: str = Form(""),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Faqat rasm fayl yuklang (jpg yoki png)")

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return crud.create_contact_request(
        db,
        full_name=full_name,
        email=email,
        phone_number=phone_number,
        user_comment=user_comment,
        file_path=file_path
    )


# ---------------------------
# READ ALL
@router.get("/", response_model=list[schemas.ContactRequestOut])
def read_contacts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_contacts(db, skip=skip, limit=limit)


# ---------------------------
# READ ONE
@router.get("/{contact_id}", response_model=schemas.ContactRequestOut)
def read_contact(contact_id: int, db: Session = Depends(get_db)):
    db_contact = crud.get_contact_by_id(db, contact_id)
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact


# ---------------------------
# DELETE
@router.delete("/{contact_id}", response_model=schemas.ContactRequestOut)
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    db_contact = crud.delete_contact(db, contact_id)
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact
