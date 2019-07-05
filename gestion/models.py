from django.db import models
from django.urls import reverse

# Create your models here.


class Unidad(models.Model):
    nombre = models.CharField(max_length=128, unique=True)
    descripcion = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = 'Unidades'

    def __str__(self):
        return f"{self.nombre}"


class Provincia(models.Model):
    cod_provincia = models.CharField(max_length=10, blank=False, default='AR-')
    provincia = models.CharField(
        max_length=50, blank=False, default='Provincia')

    class Meta:
        ordering = ['provincia']

    def __str__(self):
        return f"{self.provincia}"


class Localidad(models.Model):
    localidad = models.CharField(max_length=128)
    provincia = models.ForeignKey(
        Provincia, on_delete=models.CASCADE, related_name='provincias')

    class Meta:
        verbose_name_plural = 'Localidades'

    def __str__(self):
        return self.localidad


class EstadoPedido(models.Model):
    descripcion = models.CharField(max_length=128, unique=True)
    detalles = models.TextField(blank=True)

    def __str__(self):
        return f"{self.descripcion}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    email = models.EmailField()
    telefono = models.CharField(max_length=64)
    calle = models.CharField(max_length=64)
    numero = models.CharField(max_length=6)
    localidad = models.ForeignKey(
        Localidad, on_delete=models.CASCADE, related_name='clientes')
    detalles = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def get_email(self):
        return self.email


class Proveedor(models.Model):
    cuit = models.CharField(max_length=13, unique=True)  # 20-37524377-7
    razon_social = models.CharField(max_length=64)
    nombre_fantasia = models.CharField(max_length=128, blank=True)
    telefono = models.CharField(max_length=64)
    email = models.EmailField()
    calle = models.CharField(max_length=64)
    numero = models.CharField(max_length=4)
    localidad = models.ForeignKey(
        Localidad, on_delete=models.CASCADE, related_name='proveedores')
    detalles = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return f"{self.razon_social}"

    def get_absolute_url(self):
        return reverse('index')


class Insumo(models.Model):
    nombre = models.CharField(max_length=64, unique=True)
    descripcion = models.TextField(blank=True)
    medida = models.CharField(max_length=64)
    unidad_medida = models.ForeignKey(
        Unidad, on_delete=models.CASCADE, default=3, related_name='unidades')
    precio = models.DecimalField(
        help_text='Precio en $', max_digits=6, decimal_places=2)
    proveedores = models.ManyToManyField(Proveedor)

    def __str__(self):
        if self.descripcion:
            return f"{self.nombre} - {self.descripcion}"
        else:
            return self.nombre


class StockInsumo(models.Model):
    insumo = models.OneToOneField(Insumo, on_delete=models.CASCADE)
    cantidad = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name='Cantidad en Stock')
    detalles = models.TextField(blank=True)

    def __str__(self):
        return f"{self.cantidad} - {self.insumo}"


class Producto(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(max_length=100)
    precio = models.DecimalField(
        help_text='Precio en $', max_digits=6, decimal_places=2)
    insumos = models.ManyToManyField(Insumo, through='InsumosProducto')

    def __str__(self):
        return f"{self.nombre} - {self.descripcion}"


class InsumosProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} de {self.insumo.nombre}\
            por cada {self.producto.nombre}"


class Pedido(models.Model):
    fecha_pedido = models.DateField(auto_now_add=True)
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    estado_pedido = models.ForeignKey(
        EstadoPedido, on_delete=models.CASCADE, related_name='pedidos')
    productos_pedido = models.ManyToManyField(Producto)
    precio_final = models.DecimalField(
        help_text='Precio en $', max_digits=6, decimal_places=2)
    detalles = models.TextField(blank=True)

    def __str__(self):
        return f"Pedido #{self.id}"
