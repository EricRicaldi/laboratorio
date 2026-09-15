from pathlib import Path

import cv2
import matplotlib.pyplot as plt

from image_processing.loader import cargar_imagen
from image_processing.transform import convertir_grises, ajustar_brillo


def main():
    ruta = Path("data/imagen_prueba.jpg")

    imagen = cargar_imagen(str(ruta))

    if imagen is None:
        raise FileNotFoundError("No se pudo cargar la imagen de prueba.")

    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

    gris = convertir_grises(imagen)

    brillo = ajustar_brillo(gris, alpha=1.5, beta=50)

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(imagen_rgb)
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(gris, cmap="gray")
    plt.title("Escala de grises")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(brillo, cmap="gray")
    plt.title("Brillo ajustado")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()