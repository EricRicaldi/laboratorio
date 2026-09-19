import cv2
import numpy as np


class ImageAnalyzer:
    """Clase que encapsula la lógica de análisis de imágenes."""

    def calcular_histograma(self, imagen: np.ndarray) -> np.ndarray:
        """Calcula el histograma de una imagen en escala de grises."""
        histograma = cv2.calcHist([imagen], [0], None, [256], [0, 256])
        return histograma.flatten()

    def clasificar_imagen(self, histograma: np.ndarray) -> str:
        """Clasifica la imagen como oscura o clara según su distribución."""
        intensidad_baja = histograma[:128].sum()
        intensidad_alta = histograma[128:].sum()

        if intensidad_baja > intensidad_alta:
            return "oscura"
        return "clara"