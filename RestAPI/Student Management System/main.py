from fastapi import FastAPI

from src.router.admin_router import router as admin_router
from src.router.student_router import router as student_router

app = FastAPI()

app.include_router(student_router)
app.include_router(admin_router)