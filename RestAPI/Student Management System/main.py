from fastapi import FastAPI

from src.router.student_router import router as student_router

app = FastAPI()

app.include_router(student_router)