
"""
Pruebas automatizadas para verificar el funcionamiento
del perceptrón simple.
"""

from src.perceptron import Perceptron
from src.dataset import training_data


def test_prediction():
    """Verifica la aprobación de una solicitud favorable."""
    model = Perceptron()
    model.train(training_data)

    assert model.predict([8, 1]) == 1


def test_rejection():
    """Verifica el rechazo de una solicitud desfavorable."""
    model = Perceptron()
    model.train(training_data)

    assert model.predict([1, 0]) == 0
