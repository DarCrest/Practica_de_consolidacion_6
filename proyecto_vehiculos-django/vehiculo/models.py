from django.db import models

# Create your models here.
CATEGORIA_CHOICES = [
    ("PARTICULAR", "Particular"),
    ("TRANSPORTE", "Transporte"),
    ("CARGA", "Carga")
]


class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(
        max_length=20, default='Ford', verbose_name="Marca:")
    modelo = models.CharField(max_length=100, verbose_name="Modelo:")
    serial_carroceria = models.CharField(
        max_length=50, verbose_name="Serial de Carroseria:")
    serial_motor = models.CharField(
        max_length=50, verbose_name="Serial de Motor:")
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default=(
        "PARTICULAR", "Particular"), verbose_name="Categoria:")
    precio = models.DecimalField(
        max_digits=11, decimal_places=2, verbose_name="Precio:")
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (('visualizar_catalogo', 'Puede ver Vehiculos'),
                    ('add_vehiculomodel', 'Agregar vehiculo'))

    def __str__(self):
        return self.modelo
