# admin.py
from sqladmin import Admin, ModelView
from fastapi import FastAPI
from contact.models import ContactRequest
from database import engine, SessionLocal

app = FastAPI()

# Admin panelni ishga tushiramiz
admin = Admin(app, engine)


# ContactRequest modelini ro'yxatdan o'tkazamiz
class ContactRequestAdmin(ModelView, model=ContactRequest):
    column_list = [ContactRequest.id, ContactRequest.full_name, ContactRequest.email,
                   ContactRequest.phone_number, ContactRequest.korrupsiya,
                   ContactRequest.user_comment, ContactRequest.file_path]


admin.add_view(ContactRequestAdmin)
