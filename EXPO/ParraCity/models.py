from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=64)
    categoria = (
        ('BUENOS EJEMPLOS','Buenos Ejemplos'),
        ('URBANISMO Y VIALIDAD','Urbanismo Y Vialidad'),
        ('NEGOCIOS','Negocios'),
        ('SOCIAL','Social'),
        ('GOBIERNO','Gobierno'),
        ('SERVICIO COMUNITARIO','Servicio a la comunidad'),
        ('OBJETOS PERDIDOS','Objetos Perdidos')
    )
    categoria_post = models.CharField(max_length = 20, choices = categoria, default = 'Social')
    contenido = models.TextField()
    media = models.ImageField(upload_to = 'post_media/', blank = True, null = True)
    creacion = models.DateTimeField (default = timezone.now)
    publicacion = models.DateTimeField(blank = True, null = True)
    Slug = models.SlugField(max_length = 200, unique = True)

    def published(self):
        self.Publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
