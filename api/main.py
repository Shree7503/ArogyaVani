from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

# Set up Jinja2 template directory
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})
