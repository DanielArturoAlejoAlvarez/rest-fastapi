from typing import Optional
from fastapi import FastAPI

from models.Item import *

app=FastAPI()

@app.get('/')
def index():
  return {'msg': 'WELCOME TO FASTAPI'}

@app.get('/items/{item_id}')
def get_items(item_id: int, q: Optional[str]=None):
  return {'item_id': item_id, 'q': q}