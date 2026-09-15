import numpy as np

from image_processing.transform import ajustar_brillo, convertir_grises


def test_convertir_grises_retorna_una_matriz_de_dos_dimensiones():
    imagen = np.zeros((10, 10, 3), dtype=np.uint8)

    resultado = convertir_grises(imagen)

    assert resultado.shape == (10, 10)


def test_ajustar_brillo_mantiene_dimensiones():
    imagen = np.zeros((10, 10), dtype=np.uint8)

    resultado = ajustar_brillo(imagen, alpha=1.2, beta=30)

    assert resultado.shape == (10, 10)