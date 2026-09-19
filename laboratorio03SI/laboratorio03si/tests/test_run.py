from laboratorio03si.pipeline_registry import register_pipelines


def test_pipeline_histogram_registered():
    pipelines = register_pipelines()

    assert "histogram" in pipelines
    assert "__default__" in pipelines