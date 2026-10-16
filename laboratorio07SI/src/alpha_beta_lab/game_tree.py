
def crear_arbol() -> dict:
    """
    Crea un árbol de búsqueda con valores en sus hojas.

    Los nodos A, B y C representan decisiones.
    Los nodos D, E, F y G contienen los valores finales.
    """
    return {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": 3,
        "E": 5,
        "F": 2,
        "G": 9,
    }
