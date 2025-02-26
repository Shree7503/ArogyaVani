from fastapi import APIRouter, Request
from src.config import templates

router = APIRouter(
    prefix="/panchayat"
)

@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("panchayat.html", {"request": request})