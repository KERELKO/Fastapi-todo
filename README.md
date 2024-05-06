# FastAPI todo application

## About app
It's simple to-do application made with FastAPI and library FastAPI-Users  
to practice base CRUD with FastAPI framework, but it's also a good way to practice  
design patterns and development patterns like 'Repository'  

## Requirements 
- [FastAPI](https://fastapi.tiangolo.com/)
- [Postgresql](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [FastAPI-Users](https://fastapi-users.github.io/fastapi-users/latest/)

## Quick overview
![image](https://github.com/KERELKO/Fastapi-postgres-todo/assets/89779202/928c32ec-23cb-4031-899c-8e94713cc0ee)
## How to use
To use this app you need to clone the repository with the command 
```
git clone https://github.com/KERELKO/Fastapi-postgres-todo
``` 
if you use docker with maketools run
```
make compose
```
or 
```
docker compose up
``` 
if you don't use docker ***activate your virtual environment*** 
and install requirements with 
```
poetry install
```
or 
```
pip install -r requirements.txt
```
then run
```
uvicorn src.main:create_app --reload
```
> [!NOTE]
> Note that if you don't use docker, in ```config.py``` ```DATABASE_URL``` variable links to postgres with settings that configured in docker-compose.yaml,
> you can change it to local with sqlite database in the file,
>  also note that you need to init models manually 
## Project structure
```
.
├── poetry.lock
├── pyproject.toml
├── src
│   ├── auth
│   │   ├── config.py
│   │   ├── __init__.py
│   │   ├── manager.py
│   │   ├── routes.py
│   │   └── schemas.py
│   ├── core
│   │   ├── config.py
│   │   ├── constants.py
│   │   ├── database.py
│   │   ├── exceptions.py
│   │   ├── __init__.py
│   │   ├── middleware.py
│   │   ├── repositories
│   │   │   ├── base.py
│   │   │   └── sqlalchemy.py
│   │   └── schemas.py
│   ├── __init__.py
│   ├── main.py
│   ├── services
│   │   ├── __init__.py
│   │   └── tasks.py
│   ├── tasks
│   │   ├── exceptions.py
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── schemas.py
│   └── utils
│       ├── __init__.py
│       └── web.py
└── tests
    ├── e2e
    │   ├── conftest.py
    │   ├── __init__.py
    │   ├── test_auth.py
    │   └── test_tasks.py
    ├── __init__.py
    ├── integration
    │   ├── conftest.py
    │   ├── __init__.py
    │   └── test_repo.py
    └── unit
        ├── conftest.py
        └── __init__.py
```


## TODO:
- Better tests cover
