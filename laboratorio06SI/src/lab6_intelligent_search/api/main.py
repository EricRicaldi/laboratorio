from fastapi import FastAPI, HTTPException

from lab6_intelligent_search.models.route_models import RouteRequest
from lab6_intelligent_search.services.search_service import find_route

app = FastAPI(
    title="API de Búsqueda Inteligente",
    description="API para encontrar rutas mediante el algoritmo A*",
    version="1.0.0"
)


@app.post("/search-route")
def search_route(request: RouteRequest):
    try:
        resultado = find_route(request.start, request.goal)
        return {
            "mensaje": "Ruta encontrada correctamente",
            "resultado": resultado
        }
    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )