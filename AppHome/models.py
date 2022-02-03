from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User





# Create your models here.

class Post(models.Model):

    Fecha= models.DateTimeField(auto_now_add=True)
    Autor=models.ForeignKey(User, on_delete=models.CASCADE)
    #Autor= models.CharField(max_length=30)
    Titulo= models.CharField(max_length=20)
    Subtitulo= models.CharField(max_length=40)
    #Foto= ImageField()
    Cuerpo= RichTextField()

    def __str__(self):

        return f"Titulo: {self.Titulo} - Subtitulo: {self.Subtitulo}"
        

