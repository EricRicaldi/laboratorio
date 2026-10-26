
# Agente Académico UCV

## 1. Descripción del proyecto

Este proyecto implementa un agente académico utilizando Google Agent Development Kit (ADK) y el modelo Gemini. Su objetivo es ayudar a comprender conceptos relacionados con la Ingeniería de Sistemas mediante explicaciones en español y lenguaje sencillo.

## 2. Tecnologías utilizadas

- Python
- Google Agent Development Kit (ADK)
- Gemini API
- Poetry para la gestión de dependencias
- Pytest para las pruebas automatizadas
- Visual Studio Code como entorno de desarrollo

## 3. Funcionalidades

- Explicar conceptos básicos de Ingeniería de Sistemas.
- Reconocer conceptos registrados en la herramienta `explicar_concepto`.
- Normalizar las consultas para reconocer diferencias entre mayúsculas y minúsculas.
- Informar cuando un concepto no está registrado.
- Generar respuestas en español mediante el modelo Gemini.

## 4. Estructura del proyecto

```text
laboratorio-adk-ucv/
├── agente_ucv/
│   ├── __init__.py
│   └── agent.py
├── tests/
│   └── test_agent.py
├── .env
├── .gitignore
├── poetry.lock
├── pyproject.toml
└── README.md
```

## 5. Configuración del entorno

### Requisitos

- Python compatible con las dependencias del proyecto.
- Poetry instalado.
- Una clave válida de Gemini API con acceso al modelo configurado.

### Instalación de dependencias

```powershell
poetry install --no-root
```

### Configuración de la clave API

Crear o editar el archivo `.env` en la raíz del proyecto y agregar:

```env
GOOGLE_API_KEY=TU_CLAVE_API
```

Reemplazar `TU_CLAVE_API` por la clave propia. No publicar este archivo ni compartir la clave.

## 6. Ejecución del agente

Desde la terminal, en la carpeta raíz del proyecto, ejecutar:

```powershell
poetry run adk web
```

Abrir en el navegador:

```text
http://127.0.0.1:8000
```

Seleccionar el agente `agente_ucv` e introducir una consulta, por ejemplo:

```text
¿Qué es machine learning?
```

El agente utilizará la herramienta `explicar_concepto` y el modelo Gemini para generar una respuesta.

## 7. Pruebas automatizadas

Ejecutar las pruebas con:

```powershell
poetry run python -m pytest -v
```

Las pruebas verifican la explicación de conceptos registrados, el comportamiento ante conceptos desconocidos y el reconocimiento de consultas con mayúsculas.

En la ejecución realizada durante el desarrollo, las cuatro pruebas finalizaron correctamente.

## 8. Evidencias de funcionamiento

Las evidencias del proyecto incluyen:

- Configuración del agente académico en `agent.py`.
- Ejecución satisfactoria de las cuatro pruebas automatizadas.
- Consulta realizada desde la interfaz de ADK y respuesta generada por Gemini.

## 9. Conclusión

Se implementó y probó un agente académico que combina una herramienta propia para consultar conceptos registrados con un modelo de lenguaje Gemini. Las pruebas automatizadas y la ejecución desde la interfaz de ADK permitieron comprobar el funcionamiento de los componentes principales del proyecto.
