from sqlalchemy.exc import SQLAlchemyError
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from src.exception.resource_not_found_exception import ResourceNotFoundException

templates = Jinja2Templates(directory='src/templates')
def resource_not_found_exception_handler(request:Request,exc:ResourceNotFoundException):
    return templates.TemplateResponse(request,"error.html",{"request":request,"ex":exc.message})

def sqlalchemy_exception_handler(request:Request,exc:SQLAlchemyError):
    print(exc)
    return templates.TemplateResponse(request,"error.html",{"request":request,"exc":str(exc)})

def global_exception_handler(request:Request,exc:Exception):
    return templates.TemplateResponse(request,"error.html",{"request":request,"exc":str(exc)})

