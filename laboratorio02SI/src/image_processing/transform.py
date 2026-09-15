import cv2


def convertir_grises(imagen):
    """Convierte una imagen BGR a escala de grises."""
    return cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)


def ajustar_brillo(imagen, alpha: float = 1.2, beta: int = 30):
    """Ajusta contraste y brillo con alpha y beta."""
    return cv2.convertScaleAbs(imagen, alpha=alpha, beta=beta)