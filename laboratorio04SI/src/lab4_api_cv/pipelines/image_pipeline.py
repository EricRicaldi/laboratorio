from kedro.pipeline import node, pipeline
from kedro.io import DataCatalog, MemoryDataset
from kedro.runner import SequentialRunner

from lab4_api_cv.services.image_service import analizar_imagen


def create_pipeline(**kwargs):
    return pipeline(
        [
            node(
                func=analizar_imagen,
                inputs="path",
                outputs="resultado",
                name="analizar_imagen_node",
            )
        ]
    )


def ejecutar_pipeline(path: str):
    catalog = DataCatalog(
        {
            "path": MemoryDataset(data=path),
        }
    )

    resultados = SequentialRunner().run(
        create_pipeline(),
        catalog,
    )

    resultado = resultados["resultado"]

    # Si Kedro devuelve un MemoryDataset, extrae su contenido.
    if hasattr(resultado, "load"):
        resultado = resultado.load()

    return resultado