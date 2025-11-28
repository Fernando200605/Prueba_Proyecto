from django.db import models

# Create your models here.

class categoria(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        db_table = "categoria"

    def __str__(self):
        return self.nombre
    
class tipoelemento(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "tipoelemento"
        verbose_name_plural = "tipoelementos"
        db_table = "tipoelemento"

    def __str__(self):
        return self.nombre
    
class marca(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marcas"
        db_table = "marca"

    def __str__(self):
        return self.nombre


