import cv2
import numpy as np


def analizar_imagen_rgb(path: str):
    imagen_bgr = cv2.imread(path)

    if imagen_bgr is None:
        raise ValueError("No se pudo leer la imagen")

    # OpenCV carga la imagen en BGR; la convertimos a RGB
    imagen_rgb = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2RGB)

    # Separar los canales RGB
    r = imagen_rgb[:, :, 0]
    g = imagen_rgb[:, :, 1]
    b = imagen_rgb[:, :, 2]

    # Calcular la media de cada canal
    medias = {
        "R": float(np.mean(r)),
        "G": float(np.mean(g)),
        "B": float(np.mean(b)),
    }

    # Calcular la desviación estándar de cada canal
    desviaciones = {
        "R": float(np.std(r)),
        "G": float(np.std(g)),
        "B": float(np.std(b)),
    }

    # Calcular la participación porcentual de cada canal
    total = sum(medias.values())

    if total > 0:
        porcentajes = {
            canal: round(valor / total * 100, 2)
            for canal, valor in medias.items()
        }
    else:
        porcentajes = {
            "R": 0.0,
            "G": 0.0,
            "B": 0.0,
        }

    # Identificar el canal predominante
    canal_dominante = max(medias, key=medias.get)

    # Clasificar el color según el canal predominante
    etiquetas_color = {
        "R": "ROJIZO",
        "G": "VERDOSO",
        "B": "AZULADO",
    }

    etiqueta_color = etiquetas_color[canal_dominante]

    # Calcular el brillo promedio en escala de grises
    imagen_gris = cv2.cvtColor(imagen_rgb, cv2.COLOR_RGB2GRAY)
    brillo_promedio = float(np.mean(imagen_gris))

    # Clasificar el nivel de brillo
    if brillo_promedio < 85:
        nivel_brillo = "Bajo"
    elif brillo_promedio < 170:
        nivel_brillo = "Medio"
    else:
        nivel_brillo = "Alto"

    # Retornar todos los resultados
    return {
        "alto": int(imagen_rgb.shape[0]),
        "ancho": int(imagen_rgb.shape[1]),
        "canales": int(imagen_rgb.shape[2]),
        "media_rgb": {
            canal: round(valor, 2)
            for canal, valor in medias.items()
        },
        "desviacion_rgb": {
            canal: round(valor, 2)
            for canal, valor in desviaciones.items()
        },
        "participacion_rgb_pct": porcentajes,
        "canal_dominante": canal_dominante,
        "etiqueta_color": etiqueta_color,
        "brillo_promedio": round(brillo_promedio, 2),
        "nivel_brillo": nivel_brillo,
    }