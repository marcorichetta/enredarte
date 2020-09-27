import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from productos.models import ProductImage
from .factories import ProductoFactory

from django import forms
from PIL import Image
from io import BytesIO


class ProductImageFormTest(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = (
            "producto",
            "imagen",
        )


@pytest.mark.django_db
def test_form_imagen():

    producto_test = ProductoFactory()

    test_image = ProductImage(producto=producto_test)

    im_io = BytesIO()  # a BytesIO object for saving image
    im = Image.new(mode="RGB", size=(200, 200))  # create a new image using PIL
    im.save(im_io, "png")  # save the image to im_io
    im_io.seek(0)  # seek to the beginning

    test_image.imagen = SimpleUploadedFile("test_image.png", im_io.read(),)

    form = ProductImageFormTest({"producto": producto_test, "imagen": test_image})

    print(form.data)
    print(form.errors)
    assert form.is_valid()
    print(form.cleaned_data)

    # instance = form.save()

    test_image.save()

    assert test_image.imagen.name == "test_image.png"
