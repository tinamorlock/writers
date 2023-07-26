from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .routers import auth, oauth2, user
from . import models 
from .database import engine

from .config import settings


# this ensures the sql alchemy models are implemented and created on the database

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# add more routers here when you add more functionality

app.include_router(auth.router)
app.include_router(oauth2.router)
app.include_router(user.router)

# displays initial home page
# other pages should render from their respective routers

@app.get("/", response_class=HTMLResponse)
def get_home():
    return templates.TemplateResponse("index.html")