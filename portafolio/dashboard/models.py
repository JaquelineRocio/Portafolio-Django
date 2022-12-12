from django.db import models

class Item(models.Model):
    titulo = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='images/', default=None)
    descripcion = models.TextField(max_length=400)
    tags = models.CharField(max_length=100)
    url_github = models.URLField(max_length=200)
