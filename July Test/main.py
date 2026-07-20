from fastapi import FastAPI

from src.router.blog_router import router as blog_router
from src.router.category_router import router as category_router
from src.router.user_router import router as user_router
app = FastAPI()

app.include_router(user_router)
app.include_router(category_router)
app.include_router(blog_router)