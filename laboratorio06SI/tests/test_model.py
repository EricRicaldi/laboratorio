
import pytest

from lab6_intelligent_search.services.search_service import find_route


def test_find_route():
    resultado = find_route("A", "F")

    assert resultado["path"] == ["A", "C", "F"]
    assert resultado["cost"] == 7


def test_destino_inexistente():
    with pytest.raises(Exception):
        find_route("A", "Z")