

from jose import jwt, JWTError
from dotenv import load_dotenv
from starlette.exceptions import HTTPException

load_dotenv()
import os

def generate_token(payload:dict):
    token = jwt.encode(payload, key=os.getenv('SECRET_KEY',"jhadhhjhhjasq"),
                       algorithm=os.getenv("TOKEN_ALGO",'HS256'))
    return token

def verify_token(token:str):
    try:
        payload = jwt.decode(token, key=os.getenv('SECRET_KEY',"jhadhhjhhjasq"),
                             algorithms=os.getenv('TOKEN_ALGO',"HS256"))
        print(f"Payload : {payload}")
        return payload
    except JWTError as e:
        raise HTTPException(status_code=400, detail="Unauthorized")
