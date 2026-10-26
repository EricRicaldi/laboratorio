
from google.adk.agents.llm_agent import Agent


def explicar_concepto(concepto: str) -> dict:
    """Explica conceptos técnicos registrados."""

    conceptos = {
        "api": "Una API permite la comunicación entre sistemas.",
        "algoritmo": "Un algoritmo es una secuencia de pasos para resolver un problema.",
        "base de datos": "Una base de datos permite almacenar y organizar información.",
        "python": "Python es un lenguaje de programación de alto nivel.",
        "inteligencia artificial": "La inteligencia artificial permite crear sistemas que realizan tareas asociadas con la inteligencia humana.",
        "machine learning": "Machine learning permite que los sistemas aprendan patrones a partir de datos.",
        "poetry": "Poetry es una herramienta para gestionar dependencias y proyectos Python.",
        "github": "GitHub permite alojar repositorios y colaborar en proyectos de software."
    }

    concepto = concepto.lower().strip()

    if concepto in conceptos:
        return {
            "status": "success",
            "explicacion": conceptos[concepto]
        }

    return {
        "status": "not_found",
        "explicacion": "Concepto no registrado."
    }


root_agent = Agent(
    model="gemini-3.8-flash",
    name="agente_ucv",
    description="Agente académico UCV",
    instruction="""
    Eres un asistente académico.
    Responde en español.
    Utiliza un lenguaje sencillo y claro.
    Ayuda a comprender conceptos de ingeniería de sistemas.
    """,
    tools=[explicar_concepto],
)
if __name__ == "__main__":
    print("Agente académico UCV configurado correctamente.")