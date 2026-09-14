from laboratorio1_ia.main import suma, multiplicar, es_mayor_que_cinco


def test_suma() -> None:
    assert suma(5, 3) == 8


def test_multiplicar() -> None:
    assert multiplicar(4, 3) == 12


def test_es_mayor_que_cinco_true() -> None:
    assert es_mayor_que_cinco(8) is True


def test_es_mayor_que_cinco_false() -> None:
    assert es_mayor_que_cinco(5) is False