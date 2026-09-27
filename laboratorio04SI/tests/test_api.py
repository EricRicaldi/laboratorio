import cv2
import numpy as np

from lab4_api_cv.services.image_service import analizar_imagen


def test_analizar_imagen(tmp_path):
    ruta_imagen = tmp_path / "imagen_prueba.png"

    imagen = np.zeros((100, 100), dtype=np.uint8)
    cv2.rectangle(imagen, (20, 20), (80, 80), 255, -1)
    cv2.imwrite(str(ruta_imagen), imagen)

    resultado = analizar_imagen(str(ruta_imagen))

    assert resultado["alto"] == 100
    assert resultado["ancho"] == 100
    assert resultado["cantidad_bordes"] > 0
    assert resultado["bordes_detectados"] == 1