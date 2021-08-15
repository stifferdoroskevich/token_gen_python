from typing import Text, Dict
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import jwt
import time


app = FastAPI()


class Data(BaseModel):
    id: str
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()


JWT_SECRET = 'rAnDoMsEcReT'
JWT_ALGORITHM = 'HS256'
MONTH = 2629743 # Unix Time Stamp


@app.get('/')
async def root():
    return {'message':'FastAPI Jwt Token Generator'}


@app.get('/token')
def generate_jwt(schema: str, store_id: int, months: int = 12):
    result = encode_jwt(schema=schema, store_id=store_id, months=months)
    return result


def encode_jwt(schema: str, store_id: int, months: int) -> Dict[str, str]:
    payload = {
        "schema": schema,
        "store_id": store_id,
        "expires": time.time() + (MONTH * months)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token
