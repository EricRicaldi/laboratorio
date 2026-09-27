from pathlib import Path
import shutil

import numpy as np
from fastapi import FastAPI, UploadFile, HTTPException

from lab4_api_cv.pipelines.image_pipeline import ejecutar_pipeline

app = FastAPI()

# Ruta principal del proyecto
BASE_DIR = Path(__file__).resolve().parents[3]
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)


def normalizar_json(valor):
    """Convierte los resultados a tipos compatibles con JSON."""

    if isinstance(valor, dict):
        return {
            str(clave): normalizar_json(contenido)
            for clave, contenido in valor.items()
        }

    if isinstance(valor, (list, tuple)):
        return [normalizar_json(item) for item in valor]

    if isinstance(valor, np.ndarray):
        return valor.tolist()

    if isinstance(valor, np.generic):
        return valor.item()

    if isinstance(valor, Path):
        return str(valor)

    if valor is None or isinstance(valor, (str, int, float, bool)):
        return valor

    # Convierte otros tipos no compatibles a texto
    return str(valor)


@app.post("/analyze-image")
def analyze_image(file: UploadFile):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No se recibió ningún archivo."
        )

    # Evita que el nombre del archivo incluya rutas
    nombre_archivo = Path(file.filename).name
    ruta_imagen = DATA_DIR / nombre_archivo

    try:
        # Guarda la imagen recibida
        with open(ruta_imagen, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Ejecuta el pipeline de Kedro
        resultado = ejecutar_pipeline(str(ruta_imagen))

        # Prepara el resultado para devolverlo como JSON
        resultado = normalizar_json(resultado)

        return {
            "mensaje": "Procesamiento exitoso",
            "resultado": resultado
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Error al procesar la imagen: {error}"
        )

    finally:
        file.file.close()