from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/contact_info",
    tags=["Contact_info"]
)


class ContactOut(BaseModel):
    location: str
    email: str
    phone: str


@router.get("/", response_model=ContactOut)
async def get_contact_info():
    return {
        "location": "Toshkent shahar, Shayxontohur tumani, Abay ko’chasi 6A-Bino",
        "email": "info@tmsiti.uz",
        "phone": "+998 71 244-51-84"
    }
