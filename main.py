from fastapi import FastAPI
from database import Base, engine
from router import users, menu, submenu
from vacancies.router import router as vacancy_router
from Workers.router import router
from auth.auth import router as auth_router


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(auth_router)
app.include_router(menu.router)
app.include_router(submenu.router)
app.include_router(vacancy_router)
app.include_router(router)