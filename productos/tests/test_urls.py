# Tests para urls de productos regulares/irregulares

from django.urls import reverse
import pytest

urls = [
    ("regular:create", {}, "regular/new/"),
    ("regular:detail", {"pk": 1}, "regular/1/"),
    ("regular:update", {"pk": 1}, "regular/1/update/"),
    ("regular:delete", {"pk": 1}, "regular/1/delete/"),
    ("irregular:create", {}, "irregular/new/"),
    ("irregular:detail", {"pk": 1}, "irregular/1/"),
    ("irregular:update", {"pk": 1}, "irregular/1/update/"),
    ("irregular:delete", {"pk": 1}, "irregular/1/delete/"),
    ("insumos:create", {}, "insumos/new/"),
    ("insumos:detail", {"pk": 1}, "insumos/1/"),
    ("insumos:update", {"pk": 1}, "insumos/1/update/"),
    ("insumos:delete", {"pk": 1}, "insumos/1/delete/"),
]


@pytest.mark.parametrize("name, kwargs, path", urls)
def test_productos_urls(name, kwargs, path):

    url_to_reverse = f"productos:{name}"

    reversed_url = reverse(url_to_reverse, kwargs=kwargs)

    expected = f"/productos/{path}"

    assert reversed_url == expected
