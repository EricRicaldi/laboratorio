import cv2


class ProcesarImagen:
    def __init__(self, umbral_bajo: int = 100, umbral_alto: int = 200):
        self.umbral_bajo = umbral_bajo
        self.umbral_alto = umbral_alto

    def analizar(self, path: str) -> dict:
        imagen = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

        if imagen is None:
            raise ValueError(
                "No se pudo cargar la imagen. "
                "Verifica que sea un archivo de imagen válido."
            )

        bordes = cv2.Canny(
            imagen,
            self.umbral_bajo,
            self.umbral_alto
        )

        return {
            "alto": int(imagen.shape[0]),
            "ancho": int(imagen.shape[1]),
            "umbrales": f"{self.umbral_bajo} y {self.umbral_alto}",
            "cantidad_bordes": int(cv2.countNonZero(bordes)),
            "bordes_detectados": int(cv2.countNonZero(bordes) > 0)
        }


def analizar_imagen(path: str) -> dict:
    procesador = ProcesarImagen()
    return procesador.analizar(path)