from pathlib import Path
import shutil

from fastapi import FastAPI, UploadFile, HTTPException
from lab4_api_cv.services.image_service import analizar_imagen

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parents[3]
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)


@app.post("/analyze-image")
def analyze_image(file: UploadFile):
    path = DATA_DIR / file.filename

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        resultado = analizar_imagen(str(path))
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    return {
        "mensaje": "Procesamiento exitoso",
        "resultado": resultado
    }