from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.router.auth_router import router as auth_router
from app.router.user_router import router as user_router
from app.router.conversation_router import router as conversation_router
from app.router.message_router import router as message_router
from app.router.feedback_router import router as feedback_router
from app.router.page_router import router as page_router

app = FastAPI(
    title="SoftSkill Coach",
    version="1.0.0"
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

app.include_router(page_router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(conversation_router)
app.include_router(message_router)
app.include_router(feedback_router)