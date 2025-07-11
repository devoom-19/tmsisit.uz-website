from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    menu_uz = Column(String, nullable=False)
    menu_ru = Column(String, nullable=False)
    menu_en = Column(String, nullable=False)

    submenus = relationship("SubMenu", back_populates="menu", cascade="all, delete-orphan")


class SubMenu(Base):
    __tablename__ = "submenus"

    id = Column(Integer, primary_key=True, index=True)
    submenu_uz = Column(String, nullable=False)
    submenu_ru = Column(String, nullable=False)
    submenu_en = Column(String, nullable=False)
    pdf_file = Column(String, nullable=True)  # <-- Bu yerda fayl yo‘li yoki nomi

    menu_id = Column(Integer, ForeignKey("menus.id", ondelete="CASCADE"), nullable=False)
    menu = relationship("Menu", back_populates="submenus")
