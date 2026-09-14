def suma(a: int, b: int) -> int:
    return a + b


def multiplicar(a: int, b: int) -> int:
    return a * b


def es_mayor_que_cinco(valor: int) -> bool:
    return valor > 5


def main() -> None:
    print("Curso: Sistemas Inteligentes")
    print("Sesión 1 - Entorno reproducible con Poetry")

    a = 10
    b = 4

    resultado = suma(a, b)
    print("La suma es:", resultado)

    resultado_multiplicacion = multiplicar(a, b)
    print("La multiplicación es:", resultado_multiplicacion)

    if es_mayor_que_cinco(resultado):
        print("La suma es mayor que 5")
    else:
        print("La suma es menor o igual que 5")

    numero = int(input("Ingrese un número: "))
    print("El número ingresado es:", numero)


if __name__ == "__main__":
    main()