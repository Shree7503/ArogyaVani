from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path
from src.config import templates

router = APIRouter(
    prefix="/home"
)

# BASE_DIR = Path(__file__).resolve().parent

@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})