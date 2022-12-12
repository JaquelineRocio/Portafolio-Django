from django.db import models
from django.utils import timezone
class Item(models.Model):
    titulo = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='images/', default=None)
    descripcion = models.TextField(max_length=400)
    tags = models.CharField(max_length=100)
    url_github = models.URLField(max_length=200)


# Dirección IP y número de visitas al sitio web
class Userip(models.Model):
    ip=models.CharField(verbose_name='Dirección IP',max_length=30)    #ip address
    count=models.IntegerField(verbose_name='Visitas',default=0) # Las visitas ip
    class Meta:
        verbose_name = 'Acceder a la información del usuario'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.ip

#Total de visitas al sitio web
class VisitNumber(models.Model):
    count=models.IntegerField(verbose_name='Total de visitas al sitio web',default=0) #Total de visitas al sitio web
    class Meta:
        verbose_name = 'Total de visitas al sitio web'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.count)

class DayNumber(models.Model):
    day=models.DateField(verbose_name='Fecha',default=timezone.now)
    count=models.IntegerField(verbose_name='Número de visitas al sitio web',default=0) #Total de visitas al sitio web
    class Meta:
        verbose_name = 'Estadísticas de visitas diarias al sitio web'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.day)