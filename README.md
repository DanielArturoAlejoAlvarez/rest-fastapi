# REST FASTAPI

## Description

This repository is a Software of Development with Python.

## Virtual

Using pipenv preferably.

## Installation

Using FastAPI, Hypercorn,etc preferably.

## DataBase

Using SQLite3, PostgreSQL MySQL, MongoDB,etc.

## Apps

Using Swagger UI.

```html

```

## Usage

```html
$ git clone https://github.com/DanielArturoAlejoAlvarez/rest-fastapi.git [NAME APP] $
pipenv shell $ pipenv python src/app.py
```

Follow the following steps and you're good to go! Important:

![alt text](https://i.stack.imgur.com/Jm4Fq.gif)

## Coding

### Config

```python
DATABASE_URI='mysql+pymysql://{}:{}@{}/{}'.format(DB_USER,DB_PASSWORD,DB_HOST,DB_NAME)
```



### Models

```python
...
from pydantic import BaseModel

class City(BaseModel):
  name: str
  timezone: str
...
```

### Controllers

```python
...
@app.get('/cities')
def get_cities():
  results=[]
  for city in db:
    r=requests.get(f'http://worldtimeapi.org/api/timezone/{city["name"]}/{city["timezone"]}')
    current_time=r.json()['datetime']
    results.append({
      'name': city["name"],
      'timezone': city["timezone"],
      'current_time': current_time
    })
  return results

@app.get('/cities/{city_id}')
def get_city(city_id: int):
  return db[city_id-1]

@app.post('/cities')
def create_city(city: City):
  db.append(city.dict())
  return db[-1]

@app.get('/cities/{city_id}')
def get_city(city_id: int):
  return db[city_id-1]

@app.post('/cities')
def create_city(city: City):
  db.append(city.dict())
  return db[-1]
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/DanielArturoAlejoAlvarez/rest-fastapi. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

```

```
