from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError
from starlette.staticfiles import StaticFiles

from src.excaption import resource_not_found_handler
from src.excaption.global_exception_handler import sqlalchemy_error_handler, unkown_exception_handler
from src.excaption.resource_not_found_handler import ResourceNotFound
from src.router.comment_router import router as comment_router
from src.router.blog_router import router as blog_router
from src.router.category_router import router as category_router
from src.router.user_router import router as user_router
app = FastAPI()

app.mount("/public",StaticFiles(directory="src/public"),name="public")

app.add_exception_handler(SQLAlchemyError,sqlalchemy_error_handler)
app.add_exception_handler(ResourceNotFound,resource_not_found_handler)
app.add_exception_handler(Exception,unkown_exception_handler)

app.include_router(user_router)
app.include_router(category_router)
app.include_router(blog_router)
app.include_router(comment_router)