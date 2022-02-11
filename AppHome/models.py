from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    Fecha= models.DateTimeField(auto_now_add=True)
    Autor=models.ForeignKey(User, on_delete=models.CASCADE)
    #Autor= models.CharField(max_length=30)
    Titulo= models.CharField(max_length=40)
    Subtitulo= models.CharField(max_length=50)
    Equipo= models.CharField(max_length=30, null=True)
    Foto= models.ImageField(upload_to="imagenes", null=True)
    Cuerpo= RichTextField()

    def __str__(self):

        return f"Titulo: {self.Titulo} - Subtitulo: {self.Subtitulo}"

        
class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"

class Mensajeria(models.Model):

    Fecha = models.DateTimeField(auto_now_add=True)
    Autor = models.ForeignKey(User, on_delete=models.CASCADE)
    Asunto = models.CharField(max_length=60)
    Mensaje = RichTextField() 

    def __str__(self):

        return f"Asunto: {self.Asunto}"
