from django.contrib import messages


class DeleteSuccessMessageMixin:
    """
    Agrega un mensaje exitoso al borrar un objeto.
    """

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)

        # Enviamos el mensaje después de que el objeto haya sido borrado
        messages.success(self.request, self.success_message)

        return response
