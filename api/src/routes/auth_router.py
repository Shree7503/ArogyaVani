from fastapi import APIRouter, Request
from src.config import templates

router = APIRouter(
    prefix="/auth"
)

@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("loginpanchayat.html", {"request": request})