class Variante(models.Model):
    """ Una variante esta asociada a un Producto Base.
        Producto = Bandeja
        Variante = Bandeja 30 * 20 * 50
    """

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    precio = models.PositiveIntegerField(help_text="Precio en $")
    stock = models.IntegerField(null=True, blank=True)  # None is unlimited

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

    def get_precio(self):
        """
        Devuelve el precio de venta si existe, sino devuelve el precio normal
        """
        return self.precio_venta if self.precio_venta else self.precio

    def get_absolute_url(self):
        # URL del Producto(FK)
        return self.producto.get_absolute_url()

    def get_nombre(self):
        return f"{self.producto.nombre} - {self.nombre}"
    
""" Si no existe una variante del producto, crear
            una con ciertos parámetros."""
        if self.variante_set.all().count() == 0:
            Variante.objects.create(producto=self, precio=self.precio, nombre="Default")

def has_variants(self):
        if self.variante_set.all().count == 0:
            return False
        variantes = self.variante_set.all()
        
        return variantes