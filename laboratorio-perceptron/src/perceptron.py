
class Perceptron:
    """
    Implementación de un perceptrón simple para clasificación
    binaria de solicitudes de crédito.
    """

    def __init__(self, learning_rate=0.1):
        # Inicialización de pesos, bias y tasa de aprendizaje.
        self.weights = [0.0, 0.0]
        self.bias = 0.0
        self.learning_rate = learning_rate

    def activation(self, value):
        """Aplica la función de activación escalón."""
        return 1 if value >= 0 else 0

    def predict(self, inputs):
        """Calcula la predicción a partir de las entradas."""
        total = self.bias

        for i in range(len(inputs)):
            total += inputs[i] * self.weights[i]

        return self.activation(total)

    def train(self, training_data, epochs=20):
        """Entrena el perceptrón mediante la regla de aprendizaje."""
        for _ in range(epochs):
            for inputs, expected in training_data:
                prediction = self.predict(inputs)
                error = expected - prediction

                # Actualización de los pesos.
                for i in range(len(self.weights)):
                    self.weights[i] += (
                        self.learning_rate * error * inputs[i]
                    )

                # Actualización del sesgo.
                self.bias += self.learning_rate * error
