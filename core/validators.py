from django.core.exceptions import ValidationError
import re


def validar_cpi(cp):
    """
        Validador para CPA según nuevo sistema aplicado en 1999
        https://www.correoargentino.com.ar/formularios/cpa    
    """

    cp = str(cp)
    cp = cp.replace(" ", "")
    # if len(cp) > 8:
    #     raise ValidationError(
    #         ("%(value)s debe contener 8 o menos caracteres"), params={"value": cp},
    #     )

    # regex = r"([a-zA-Z]{1}\d{4}[a-zA-Z]{3}|\d{4})"

    regex = r"\d{4}"
    match = re.match(regex, cp)

    if match:
        return True
    else:
        raise ValidationError(
            ("%(value)s no es un CP válido"), params={"value": cp},
        )

    # raise ValidationError(
    #     ("%(value)s no es un CP válido"), params={"value": cp},
    # )
