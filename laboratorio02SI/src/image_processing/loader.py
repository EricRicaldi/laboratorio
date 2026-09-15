import cv2


def cargar_imagen(ruta: str):
    """Carga una imagen desde la ruta indicada."""
    return cv2.imread(ruta)