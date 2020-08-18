import re
from django import template
from django.urls import reverse, NoReverseMatch

""" To be a valid tag library, the module must contain a
    module-level variable named register that is a template.Library """
register = template.Library()


@register.simple_tag(takes_context=True)
def active(context, url_name):
    """ Se ejecutan todas las tags que tengan {% active %} en el html .
        La que cumple con el regex devuelve `active` y se pone como clase html """

    # Try to reverse the url
    try:
        url = "^" + reverse(url_name)
    except NoReverseMatch:
        # '/' doesn't reverse so only the 'index' page enters here
        url = "^" + url_name + "$"

    # Search in the context to get the routes path
    # '/pedidos/ for example
    path = context["request"].path

    if re.search(url, path):
        return "active"
    return ""
