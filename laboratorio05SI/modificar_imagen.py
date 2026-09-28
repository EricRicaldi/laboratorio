import cv2

# Leer la imagen original
imagen = cv2.imread("data/manzana.png")

if imagen is None:
    raise ValueError("No se pudo leer la imagen original")

# Aumentar el brillo sin modificar la imagen original
imagen_modificada = cv2.convertScaleAbs(
    imagen,
    alpha=1.0,
    beta=50
)

# Guardar la copia modificada
cv2.imwrite("data/manzana_modificada.png", imagen_modificada)

print("Imagen modificada y guardada correctamente.")