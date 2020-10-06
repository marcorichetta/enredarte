from django.forms import DateTimeInput, DateInput
from django_filters.widgets import SuffixedMultiWidget


class DateTimePicker(DateTimeInput):
    """ Selector personalizado de datetimes que utiliza TempusDominus junto con Bootstrap """

    template_name = "widgets/bootstrap_datetimepicker.html"

    def get_context(self, name, value, attrs):
        datetimepicker_id = "datetimepicker_{name}".format(name=name)
        attrs = attrs or {}
        attrs["data-target"] = "#{id}".format(id=datetimepicker_id)
        attrs["class"] = "form-control datetimepicker-input"
        context = super().get_context(name, value, attrs)
        context["widget"]["datetimepicker_id"] = datetimepicker_id
        return context


class DatePicker(DateInput):
    """ Selector personalizado de fechas que utiliza TempusDominus junto con Bootstrap """

    template_name = "widgets/bootstrap_datepicker.html"

    def get_context(self, name, value, attrs):
        datetimepicker_id = "datetimepicker_{name}".format(name=name)
        attrs = attrs or {}
        attrs["data-target"] = "#{id}".format(id=datetimepicker_id)
        attrs["class"] = "form-control datetimepicker-input"
        context = super().get_context(name, value, attrs)
        context["widget"]["datetimepicker_id"] = datetimepicker_id
        return context


class MultiDatePicker(SuffixedMultiWidget):
    """ Selector de rangos de fechas que utiliza el selector `DatePicker` como widget """

    template_name = "widgets/bootstrap_multiwidget.html"
    suffixes = ["min", "max"]

    def __init__(self, attrs=None):
        widgets = (DatePicker, DatePicker)
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.start, value.stop]
        return [None, None]
