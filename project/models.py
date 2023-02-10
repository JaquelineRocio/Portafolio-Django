from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls  import reverse
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=150)
    descripcion = models.TextField()
    foto_img = models.ImageField(upload_to="images",blank=True,null=True)
    url_git = models.CharField(max_length=500)
    tags = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("get-project", kwargs={"pk": self.pk})

    def save(self):
        super().save()
        if self.foto_img:
            foto_img = Image.open(self.foto_img.path)
            if foto_img.height > 300 or foto_img.width > 300:
                output_size = (300, 300)
                foto_img.thumbnail(output_size)
                foto_img.save(self.foto_img.path)
