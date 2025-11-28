from django.db import models

# Create your models here.

class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidades de Medida"
        db_table = "unidadmedida"

    def __str__(self):
        return self.nombre
class Elemento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    stockActual = models.IntegerField()
    stockMinimo = models.IntegerField()
    tipoElementoId = models.ForeignKey(tipoelemento, on_delete=models.CASCADE)
    categoriaId = models.ForeignKey(categoria, on_delete=models.CASCADE)
    marcaId = models.ForeignKey(marca, on_delete=models.CASCADE)
    unidadMedidaId = models.ForeignKey(unidadmedida, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=100)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Elemento"
        verbose_name_plural = "Elementos"
        db_table = "elemento"

    def __str__(self):
        return self.nombre

