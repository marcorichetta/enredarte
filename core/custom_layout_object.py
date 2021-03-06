# https: // stackoverflow.com/a/22053952/6389248

from crispy_forms.layout import LayoutObject, TEMPLATE_PACK
from django.template.loader import render_to_string


class Formset(LayoutObject):
    """ Renderiza un formset completo como si fuese un Field de un form.

    Ejemplos:
        Formset('contact_formset')
    """

    template = "formset.html"

    def __init__(self, formset_name_in_context, template=None):

        self.formset_name_in_context = formset_name_in_context

        # crispy_forms/layout.py:302 requires us to have a fields property
        self.fields = []

        # Overrides class variable with an instance level variable
        if template:
            self.template = template

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        formset = context.get(self.formset_name_in_context)

        context.update({"formset": formset})
        return render_to_string(self.template, context.flatten())
