from fastapi import FastAPI
from models.City import *

app=FastAPI()

db=[]

@app.get('/')
def index():
  return {
    'msg': 'WELCOME TO FASTAPI'
  }

from controllers.CityController import *