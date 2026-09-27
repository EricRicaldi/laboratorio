import cv2


def analizar_imagen(path: str):
    imagen = cv2.imread(path, 0)

    if imagen is None:
        raise ValueError(
            "No se pudo cargar la imagen. "
            "Verifica que sea un archivo de imagen válido."
        )

    # Detectar bordes usando los umbrales 100 y 200
    bordes = cv2.Canny(imagen, 100, 200)

    return {
        "alto": imagen.shape[0],
        "ancho": imagen.shape[1],
        "umbrales": "100 y 200",
        "cantidad_bordes": int(cv2.countNonZero(bordes)),
        "bordes_detectados": int(bordes.sum() > 0)
    }