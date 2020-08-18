from django.contrib import admin
from .models import Cliente

# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    # https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
    # Modificar el qs para que muestre los objetos que fueron eliminados
    def get_queryset(self, request):
        return Cliente.all_objects.all()

    list_display = (
        "id",
        "nombre",
        "apellido",
        "email",
        "telefono",
        "calle",
        "numero",
        "localidad",
        "created",
        "modified",
        "is_removed",
    )

    search_fields = ("nombre", "apellido")
    list_filter = ("created", "modified", "is_removed", "localidad")
    list_display_links = ("nombre",)
