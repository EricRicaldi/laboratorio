# Perceptrón Simple – Aprobación de Créditos

## 1. Descripción del proyecto

Este proyecto implementa desde cero un perceptrón simple utilizando Python para realizar la clasificación preliminar de solicitudes de crédito bancario.

El modelo utiliza dos características de entrada:

- **Ingreso mensual:** representa el nivel de ingresos del solicitante.
- **Historial crediticio:** representa el comportamiento crediticio del solicitante.

A partir de estos datos, el perceptrón aprende mediante un proceso de entrenamiento y genera una predicción que indica si el crédito debe ser aprobado o rechazado.

## 2. Objetivo

Implementar y comprender el funcionamiento de una neurona artificial mediante un perceptrón simple, aplicando el aprendizaje supervisado a un problema de clasificación binaria.

## 3. Tecnologías utilizadas

- Python 3.12
- Git y GitHub
- pytest
- pytest-cov
- GitHub Actions
- SonarCloud

## 4. Estructura del proyecto

```text
laboratorio-perceptron/
│
├── src/
│   ├── dataset.py
│   └── perceptron.py
│
├── tests/
│   └── test_perceptron.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── main.py
├── .gitignore
├── sonar-project.properties
└── README.md
```

## 5. Instalación

Clonar el repositorio y acceder a la carpeta del proyecto:

```bash
git clone https://github.com/EricRicaldi/laboratorio.git
cd laboratorio/laboratorio-perceptron
```

Instalar las dependencias necesarias:

```bash
python -m pip install pytest pytest-cov
```

## 6. Ejecución del programa

Para ejecutar el programa principal:

```bash
python main.py
```

El programa entrena el perceptrón utilizando el conjunto de datos definido en `src/dataset.py` y realiza una predicción con los valores de entrada `[9, 1]`.

El resultado esperado es:

```text
Resultado de la evaluación del crédito:
Crédito aprobado.
```

## 7. Ejecución de pruebas automatizadas

Para ejecutar las pruebas:

```bash
python -m pytest tests -v
```

Para generar el reporte de cobertura:

```bash
python -m pytest --cov=src --cov=main --cov-report=term-missing tests -v
```

Las pruebas verifican el funcionamiento del perceptrón, la aprobación y el rechazo de solicitudes, así como la ejecución del programa principal.

## 8. Integración continua y análisis de calidad

El proyecto utiliza GitHub Actions para automatizar la instalación de dependencias, la ejecución de pruebas y el análisis del código mediante SonarCloud.

El flujo de integración continua se encuentra en:

`.github/workflows/ci.yml`

## 9. Resultados obtenidos

- Implementación del algoritmo Perceptrón Simple.
- Ejecución correcta del programa principal.
- Cinco pruebas automatizadas superadas.
- Cobertura de código del 100 % en el último análisis de SonarCloud.
- Ejecución satisfactoria del workflow de GitHub Actions.

## 10. Autor

Proyecto desarrollado como parte del laboratorio de Sistemas Inteligentes.