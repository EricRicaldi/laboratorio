# Travel ADK Multiagent

Laboratorio UCV de desarrollo de un sistema multiagente de asistencia para viajes utilizando Google Agent Development Kit (ADK) y Gemini.

## 1. Agentes del sistema

El proyecto está compuesto por cinco agentes especializados:

- **Travel Coordinator Agent:** coordina las solicitudes y distribuye las tareas entre los agentes.
- **Web Search Agent:** proporciona información sobre destinos turísticos y recomendaciones de viaje.
- **Itinerary Agent:** organiza itinerarios de viaje según los días disponibles.
- **Budget Agent:** estima los gastos y el presupuesto del viaje.
- **Risk Reviewer Agent:** identifica posibles riesgos según el destino y la temporada.

## 2. Tecnologías utilizadas

- Python 3.11
- Google Agent Development Kit (ADK)
- Google Gemini
- Poetry
- Pytest
- Ruff
- Git y GitHub
- GitHub Actions

## 3. Instalación

Clonar el repositorio y acceder a la carpeta del proyecto.

Instalar las dependencias:

```bash
pip install poetry
poetry install
```

## 4. Variables de entorno

Crear un archivo `.env` tomando como referencia `.env.example` y configurar la variable:

```env
GOOGLE_API_KEY="TU_API_KEY"
```

**Importante:** No compartir ni subir el archivo `.env` al repositorio.

## 5. Ejecución del sistema

### Ejecutar el agente por consola

```bash
poetry run adk run travel_assistant
```

### Ejecutar la interfaz web

```bash
poetry run adk web --port 8000
```

Abrir en el navegador:

http://localhost:8000

## 6. Pruebas automatizadas

Ejecutar las pruebas:

```bash
poetry run pytest -v
```

El proyecto cuenta con seis pruebas automatizadas para validar las herramientas de presupuesto y evaluación de riesgos.

## 7. Análisis de calidad del código

Ejecutar Ruff:

```bash
poetry run ruff check .
```

## 8. Integración continua (CI)

El proyecto utiliza GitHub Actions para automatizar las siguientes tareas:

- Preparación del entorno Python.
- Instalación de Poetry y dependencias.
- Ejecución de pruebas automatizadas con Pytest.
- Análisis estático del código mediante Ruff.

El workflow se encuentra en:

`.github/workflows/ci.yml`

## 9. Resultados

- Seis pruebas automatizadas aprobadas.
- Validación de código con Ruff completada correctamente.
- Workflow de GitHub Actions ejecutado satisfactoriamente.

## 10. Autor

Proyecto académico desarrollado para la Universidad César Vallejo (UCV).