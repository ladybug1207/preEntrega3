from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad} {self.direccion}"

class Producto(models.Model):
    id_Producto = models.CharField(max_length=5)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.id_Producto} {self.nombre} {self.precio}"

class Cliente(models.Model):
    cliente = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.cliente} {self.email}"

class Vendedor(models.Model):
    id_vendedor = models.CharField(max_length=5)
    vendedor = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)
    sucursal = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.id_vendedor} {self.vendedor} {self.sucursal}"
