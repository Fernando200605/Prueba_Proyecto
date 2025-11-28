from django.db import models

# Create your models here.
class Movimiento(models.Model):
    tipo = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    cantidad = models.IntegerField()
    elementoId = models.ForeignKey(Elemento, on_delete=models.CASCADE)
    usuarioId = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cursoId = models.ForeignKey(Curso, on_delete=models.CASCADE)
    motivo = models.TextField()
    
    class Meta:
        verbose_name= 'Movimiento'
        verbose_name_plural= 'Movimiento'
        db_table= 'movimiento'

    def __str__(self):
        return self.tipo
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField()
    creadoPorUsuarioId = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        db_table = 'evento'

    def __str__(self):
        return self.titulo