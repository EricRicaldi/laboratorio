
from agente_ucv.agent import explicar_concepto


def test_explicar_concepto_api():
    resultado = explicar_concepto("api")

    assert resultado["status"] == "success"
    assert "API" in resultado["explicacion"]


def test_explicar_concepto_python():
    resultado = explicar_concepto("python")

    assert resultado["status"] == "success"
    assert "Python" in resultado["explicacion"]


def test_concepto_no_registrado():
    resultado = explicar_concepto("concepto_desconocido")

    assert resultado["status"] == "not_found"
    assert resultado["explicacion"] == "Concepto no registrado."


def test_concepto_mayusculas():
    resultado = explicar_concepto("PYTHON")

    assert resultado["status"] == "success"
