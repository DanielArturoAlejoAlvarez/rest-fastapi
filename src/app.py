from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def index():
  return {'msg': 'WELCOME TO FASTAPI'}