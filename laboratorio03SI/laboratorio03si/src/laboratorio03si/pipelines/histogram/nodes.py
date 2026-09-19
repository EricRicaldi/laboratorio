import cv2

from laboratorio03si.pipelines.histogram.analyzer import ImageAnalyzer


def analizar_imagen(filepath: str) -> dict:
    """Carga una imagen, calcula el histograma y devuelve el análisis."""
    imagen = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

    if imagen is None:
        raise ValueError(f"No se pudo cargar la imagen: {filepath}")

    analyzer = ImageAnalyzer()
    histograma = analyzer.calcular_histograma(imagen)
    clasificacion = analyzer.clasificar_imagen(histograma)

    return {
        "ruta_imagen": filepath,
        "clasificacion": clasificacion,
        "histograma": histograma.tolist(),
    }