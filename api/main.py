from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

# Ensure FastAPI correctly locates the templates folder
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})
