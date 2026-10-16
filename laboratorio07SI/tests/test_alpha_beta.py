
from alpha_beta_lab.game_tree import crear_arbol
from alpha_beta_lab.minimax import minimax
from alpha_beta_lab.alpha_beta import alpha_beta


def test_crear_arbol():
    arbol = crear_arbol()

    assert "A" in arbol
    assert arbol["A"] == ["B", "C"]


def test_minimax_arbol_basico():
    arbol = crear_arbol()

    resultado = minimax(
        arbol=arbol,
        nodo="A",
        profundidad=3,
        es_maximizador=True,
    )

    assert resultado == 3


def test_alpha_beta_arbol_basico():
    arbol = crear_arbol()

    resultado = alpha_beta(
        arbol=arbol,
        nodo="A",
        profundidad=3,
        alpha=float("-inf"),
        beta=float("inf"),
        es_maximizador=True,
    )

    assert resultado == 3


def test_minimax_y_alpha_beta_obtienen_el_mismo_valor():
    arbol = crear_arbol()

    resultado_minimax = minimax(
        arbol=arbol,
        nodo="A",
        profundidad=3,
        es_maximizador=True,
    )

    resultado_alpha_beta = alpha_beta(
        arbol=arbol,
        nodo="A",
        profundidad=3,
        alpha=float("-inf"),
        beta=float("inf"),
        es_maximizador=True,
    )

    assert resultado_minimax == resultado_alpha_beta
