from sqlalchemy import Column, Integer, String
from database import Base


class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False)
    position = Column(String(100), nullable=False)
    phone_number = Column(String(20))
    email = Column(String(100))
    avatar = Column(String(255), nullable=False)
