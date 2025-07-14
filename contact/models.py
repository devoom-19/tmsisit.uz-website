from sqlalchemy import Column, Integer, String
from database import Base


class ContactRequest(Base):
    __tablename__ = "contact_user"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False)
    phone_number = Column(String(20))
    korrupsiya = Column(String(255), default="Korrupsiyaga qarshi kurash")
    user_comment = Column(String(500))
    file_path = Column(String(255), nullable=False)  # yuklangan pdf fayl yo'li
