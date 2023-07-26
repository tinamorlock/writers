from fastapi import FastAPI
# from .routers import (add router file imports here)
from . import models 
from .database import engine

from .config import settings


# this ensures the sql alchemy models are implemented and created on the database

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# add more routers here when you add more functionality

# app.include_router(nameOfRouter.router)

# generic index. you can remove this.

@app.get("/")
def get_home():
    return {'message': 'This is the home page.'}