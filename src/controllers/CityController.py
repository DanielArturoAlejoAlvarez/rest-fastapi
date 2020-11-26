from app import *

@app.get('/cities')
def get_cities():
  return db

@app.get('/cities/{city_id}')
def get_city(city_id: int):
  return db[city_id-1]

@app.post('cities')
def create_city(city: City):
  db.append(city.dict())
  return db[-1]