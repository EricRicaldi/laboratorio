
"""
Pruebas automatizadas para verificar el funcionamiento
del perceptrón simple y del programa principal.
"""

import runpy

from src.perceptron import Perceptron
from src.dataset import training_data
from main import main


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


def test_main(capsys):
    """Verifica la ejecución y el mensaje de aprobación."""
    main()

    captured = capsys.readouterr()

    assert "Resultado de la evaluación del crédito:" in captured.out
    assert "Crédito aprobado." in captured.out


def test_main_rejection(monkeypatch, capsys):
    """Verifica la ejecución de la rama de crédito rechazado."""

    # Simular una predicción negativa para probar la rama else.
    monkeypatch.setattr(
        "main.Perceptron.predict",
        lambda self, inputs: 0
    )

    main()
    captured = capsys.readouterr()

    assert "Crédito rechazado." in captured.out


def test_module_execution(capsys):
    """Verifica la ejecución directa del archivo main.py."""

    runpy.run_path("main.py", run_name="__main__")

    captured = capsys.readouterr()

    assert "Resultado de la evaluación del crédito:" in captured.out
    assert "Crédito aprobado." in captured.out
