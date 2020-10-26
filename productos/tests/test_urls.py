# Tests para urls de productos regulares/irregulares

from django.urls import reverse


def test_urls():

    # PRODUCTOS
    assert reverse("productos:list") == "/productos/"

    assert reverse("productos:regular-create") == "/productos/regular/new/"
    assert (
        reverse("productos:regular-detail", kwargs={"pk": 1}) == "/productos/regular/1/"
    )
    assert (
        reverse("productos:regular-update", kwargs={"pk": 1})
        == "/productos/regular/1/update/"
    )
    assert (
        reverse("productos:regular-delete", kwargs={"pk": 1})
        == "/productos/regular/1/delete/"
    )

    assert reverse("productos:irregular-create") == "/productos/irregular/new/"
    assert (
        reverse("productos:irregular-detail", kwargs={"pk": 1})
        == "/productos/irregular/1/"
    )
    assert (
        reverse("productos:irregular-update", kwargs={"pk": 1})
        == "/productos/irregular/1/update/"
    )
    assert (
        reverse("productos:irregular-delete", kwargs={"pk": 1})
        == "/productos/irregular/1/delete/"
    )

    # INSUMOS
    assert reverse("productos:insumos-list") == "/productos/insumos/"
    assert reverse("productos:insumos-create") == "/productos/insumos/new/"
    assert (
        reverse("productos:insumos-detail", kwargs={"pk": 1}) == "/productos/insumos/1/"
    )
    assert (
        reverse("productos:insumos-update", kwargs={"pk": 1})
        == "/productos/insumos/1/update/"
    )
    assert (
        reverse("productos:insumos-delete", kwargs={"pk": 1})
        == "/productos/insumos/1/delete/"
    )
