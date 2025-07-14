from fastapi import FastAPI
from sqladmin import Admin, ModelView
from database import Base, engine
from router import users, menu, submenu
from vacancies.router import router as vacancy_router
from Workers.router import router
from info_contact import router as contact_router
from contact.router import router as user_contact_router
from auth.auth import router as auth_router
from contact.models import ContactRequest
from database import engine


app = FastAPI()


# Admin panel
admin = Admin(app, engine)


class ContactRequestAdmin(ModelView, model=ContactRequest):
    column_list = [ContactRequest.id, ContactRequest.full_name, ContactRequest.email,
                   ContactRequest.phone_number, ContactRequest.korrupsiya,
                   ContactRequest.user_comment, ContactRequest.file_path]


admin.add_view(ContactRequestAdmin)


Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(auth_router)
app.include_router(menu.router)
app.include_router(submenu.router)
app.include_router(vacancy_router)
app.include_router(router)
app.include_router(contact_router)
app.include_router(user_contact_router)