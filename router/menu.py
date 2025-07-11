from fastapi import APIRouter, Depends, Query
from fastapi import Depends, HTTPException, Query
from sqlalchemy.orm import Session
from auth.security import get_current_user
from database import SessionLocal
import models, schemas




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/menus", tags=["Menus"])

@router.post("/menus/", response_model=schemas.MenuOut)
def create_menu(menu: schemas.MenuCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_menu = models.Menu(**menu.dict())
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return {"id": db_menu.id, "menu": db_menu.menu_uz}

@router.get("/menus/", response_model=list[schemas.MenuOut])
def read_menus(lang: str = Query("uz", enum=["uz", "ru", "en"]), db: Session = Depends(get_db)):
    menus = db.query(models.Menu).all()
    return [{"id": m.id, "menu": getattr(m, f"menu_{lang}")} for m in menus]

@router.get("/menus/{menu_id}", response_model=schemas.MenuOut)
def read_menu(menu_id: int, lang: str = Query("uz", enum=["uz", "ru", "en"]), db: Session = Depends(get_db)):
    menu = db.query(models.Menu).filter(models.Menu.id == menu_id).first()
    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")
    return {"id": menu.id, "menu": getattr(menu, f"menu_{lang}")}

@router.put("/menus/{menu_id}", response_model=schemas.MenuOut)
def update_menu(menu_id: int, menu_update: schemas.MenuUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    menu = db.query(models.Menu).filter(models.Menu.id == menu_id).first()
    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")
    for field, value in menu_update.dict().items():
        setattr(menu, field, value)
    db.commit()
    db.refresh(menu)
    return {"id": menu.id, "menu": menu.menu_uz}

@router.delete("/menus/{menu_id}", status_code=204)
def delete_menu(menu_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    menu = db.query(models.Menu).filter(models.Menu.id == menu_id).first()
    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")
    db.delete(menu)
    db.commit()
    return None