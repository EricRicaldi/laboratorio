
"""
Programa principal para entrenar y probar el perceptrón simple.
"""

from src.perceptron import Perceptron
from src.dataset import training_data


def main():
    # Crear el modelo de perceptrón.
    model = Perceptron()

    # Entrenar el modelo con los datos definidos.
    model.train(training_data)

    # Realizar una predicción para una nueva solicitud.
    prediction = model.predict([9, 1])

    # Mostrar el resultado de la clasificación.
    print("Resultado de la evaluación del crédito:")

    if prediction == 1:
        print("Crédito aprobado.")
    else:
        print("Crédito rechazado.")


if __name__ == "__main__":
    main()
