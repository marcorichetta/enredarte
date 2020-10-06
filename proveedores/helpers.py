from django.core.exceptions import ValidationError

""" https://es.wikipedia.org/wiki/Clave_%C3%9Anica_de_Identificaci%C3%B3n_Tributaria#C%C3%B3digo_Python """


def validar_cuit(cuit):
    cuit = str(cuit)
    cuit = cuit.replace("-", "")
    cuit = cuit.replace(" ", "")
    if len(cuit) != 11:
        raise ValidationError(
            ("%(value)s debe contener 11 dígitos"), params={"value": cuit},
        )
    if not cuit.isdigit():
        raise ValidationError(
            ("%(value)s debe contener sólo dígitos"), params={"value": cuit},
        )
    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    aux = 0
    for i in range(10):
        aux += int(cuit[i]) * base[i]
    aux = 11 - (aux % 11)
    if aux == 11:
        aux = 0
    if int(cuit[10]) == aux:
        return True
    else:
        raise ValidationError(
            ("%(value)s no es un CUIT válido"), params={"value": cuit},
        )
