from pydantic import BaseModel
from typing import Optional


class MenuBase(BaseModel):
    menu_uz: str
    menu_ru: str
    menu_en: str


class MenuCreate(MenuBase):
    pass


class MenuUpdate(MenuBase):  # Mana shu klassni qo‘shish kerak
    pass


class MenuOut(BaseModel):
    id: int
    menu: str

    class Config:
        orm_mode = True


class SubMenuBase(BaseModel):
    submenu_uz: str
    submenu_ru: str
    submenu_en: str
    menu_id: int
    pdf_file: Optional[str]  # Bu fayl yo‘li


class SubMenuCreate(SubMenuBase):
    pass


class SubMenuUpdate(SubMenuBase):  # Mana shu klass ham kerak
    pass


class SubMenuOut(BaseModel):
    id: int
    submenu_uz: str
    submenu_ru: str
    submenu_en: str
    pdf_file: Optional[str] = None
    menu_id: int

    class Config:
        form_attributes = True