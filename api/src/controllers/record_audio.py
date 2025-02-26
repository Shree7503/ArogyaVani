from fastapi import File, UploadFile
from fastapi.responses import JSONResponse
import os

UPLOAD_FOLDER = "src/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

async def upload_audio(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_path, "wb") as audio_file:
            audio_file.write(await file.read())

        return JSONResponse(content={"message": "Audio uploaded successfully", "path": file_path}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)