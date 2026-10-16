
def minimax(
    arbol: dict,
    nodo: str,
    profundidad: int,
    es_maximizador: bool,
) -> int:
    """
    Ejecuta el algoritmo Minimax sobre un árbol de búsqueda.

    arbol: diccionario que representa los nodos y sus hijos.
    nodo: nodo actual.
    profundidad: niveles restantes de búsqueda.
    es_maximizador: indica si el turno corresponde a Max.
    """

    # Si el nodo es una hoja, devuelve su valor.
    if isinstance(arbol[nodo], int):
        return arbol[nodo]

    # Si se alcanza la profundidad indicada, devuelve 0.
    if profundidad <= 0:
        return 0

    hijos = arbol[nodo]

    # Turno del jugador Max: elige el valor mayor.
    if es_maximizador:
        mejor_valor = float("-inf")

        for hijo in hijos:
            valor = minimax(
                arbol,
                hijo,
                profundidad - 1,
                False,
            )
            mejor_valor = max(mejor_valor, valor)

        return int(mejor_valor)

    # Turno del jugador Min: elige el valor menor.
    mejor_valor = float("inf")

    for hijo in hijos:
        valor = minimax(
            arbol,
            hijo,
            profundidad - 1,
            True,
        )
        mejor_valor = min(mejor_valor, valor)

    return int(mejor_valor)
