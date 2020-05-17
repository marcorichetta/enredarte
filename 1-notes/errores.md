## Errores

---

### AttributeError: 'ManyToManyField' object has no attribute 'm2m_reverse_field_name' (**Pérdida de datos**)

[Solución](https://stackoverflow.com/a/37701209/6389248)

### ValueError: Related model 'proveedores.Proveedor' cannot be resolved (**Pérdida de datos**)

El modelo Proveedor no fue creado en la app proveedores al momento de correr
esta migración.

1. Borrar archivos de migración (Todos los creados)
2. Comentar el campo ManyToMany en cuestión
3. `makemigrations`
4. `migrate`

### ValueError: (you cannot alter to or from M2M fields, or add or remove through= on M2M fields)

No se pueden modificar ManyToMany fields. [StackOverflow](https://stackoverflow.com/questions/26927705/django-migration-error-you-cannot-alter-to-or-from-m2m-fields-or-add-or-remove)

1. Comentar el campo ManyToMany en el modelo
2. Hacer la migración
3. Quitar el comentario
4. Nuevamente hacer la migración

_Básicamente estamos eliminando y volviendo a crear el campo.
Esto posiblemente conlleve a pérdida de información ya que la
tabla que relaciona los MaM será eliminada en la primera migración._
