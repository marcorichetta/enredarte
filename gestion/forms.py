from django import forms
from django_select2.forms import ModelSelect2Widget

from .models import Localidad, Provincia

class FormPrueba(forms.Form):
    provincia = forms.ModelChoiceField(
        queryset=Provincia.objects.all(),
        label=u"Provincia",
        widget=ModelSelect2Widget(
            model=Provincia,
            search_fields=['provincia__icontains'],
        )
    )

    localidad = forms.ModelChoiceField(
        queryset=Localidad.objects.all(),
        label=u"Localidad",
        widget=ModelSelect2Widget(
            model=Localidad,
            search_fields=['localidad__icontains'],
            dependent_fields={'provincia': 'provincia'},
            max_results=10,
        )
    )
