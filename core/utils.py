from typing import List, Dict

# https://stackoverflow.com/a/62744916/6389248


def build_formset_form_data(prefix: str, form_number: int, **data) -> dict:

    form: Dict = {}
    for key, value in data.items():
        form_key = f"{prefix}-{form_number}-{key}"
        form[form_key] = value

    return form


def build_formset_data(prefix: str, forms: List[Dict], **common_data) -> dict:
    """ 
        It returns a nested dict with each formset properly formatted. For example:
        {
            'formset_prefix-TOTAL_FORMS': '2',
            'formset_prefix-MAX_NUM_FORMS': '1000',
            'formset_prefix-INITIAL_FORMS': '1',
            "formset_prefix-0-key1": "value",
            "formset_prefix-0-key2": "value",
            "formset_prefix-1-key1": "value",
            "formset_prefix-1-key2": "value",
        }
    """

    formset_dict = {
        f"{prefix}-TOTAL_FORMS": len(forms),
        f"{prefix}-MIN_NUM_FORMS": 0,
        f"{prefix}-MAX_NUM_FORMS": 1000,
        f"{prefix}-INITIAL_FORMS": 1,
    }

    formset_dict.update(common_data)

    for i, form_data in enumerate(forms):
        form_dict = build_formset_form_data(prefix=prefix, form_number=i, **form_data)
        formset_dict.update(form_dict)

    return formset_dict
