from fastapi import APIRouter, File, UploadFile
from src.controllers.record_audio import upload_audio

router = APIRouter(
    prefix="/upload"
)

@router.post("/")
async def index(file: UploadFile = File(...)):
    return await upload_audio(file)