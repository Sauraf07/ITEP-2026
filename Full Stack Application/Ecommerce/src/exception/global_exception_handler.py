from sqlalchemy.exc import SQLAlchemyError
from starlette.requests import Request
from starlette.responses import JSONResponse
from src.exception.resource_not_found_exception import ResourceNotFoundException

def resource_not_found_exception_handler(request:Request,exc:ResourceNotFoundException):
    return JSONResponse(status_code=404,
                        content={
                            "error": "Not found",
                            "message": exc.message
                        })

def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    print(exc)
    return JSONResponse(
        status_code=500,
        content={
            "error":"Database error",
            "message":str(exc),
        }
    )

def unknown_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error":"Internal Server Error","message":str(exc)})
