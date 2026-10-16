
def alpha_beta(
    arbol: dict,
    nodo: str,
    profundidad: int,
    alpha: float,
    beta: float,
    es_maximizador: bool,
) -> int:
    """
    Ejecuta Alpha-Beta sobre un árbol de búsqueda.
    """

    # Si el nodo es una hoja, devuelve su valor.
    if isinstance(arbol[nodo], int):
        return arbol[nodo]

    # Si se alcanza la profundidad indicada, devuelve 0.
    if profundidad <= 0:
        return 0

    hijos = arbol[nodo]

    # Turno de Max: busca el valor más alto.
    if es_maximizador:
        mejor_valor = float("-inf")

        for hijo in hijos:
            valor = alpha_beta(
                arbol,
                hijo,
                profundidad - 1,
                alpha,
                beta,
                False,
            )

            mejor_valor = max(mejor_valor, valor)
            alpha = max(alpha, mejor_valor)

            # Poda de ramas que ya no pueden mejorar el resultado.
            if beta <= alpha:
                break

        return int(mejor_valor)

    # Turno de Min: busca el valor más bajo.
    mejor_valor = float("inf")

    for hijo in hijos:
        valor = alpha_beta(
            arbol,
            hijo,
            profundidad - 1,
            alpha,
            beta,
            True,
        )

        mejor_valor = min(mejor_valor, valor)
        beta = min(beta, mejor_valor)

        # Poda de ramas que ya no pueden mejorar el resultado.
        if beta <= alpha:
            break

    return int(mejor_valor)
