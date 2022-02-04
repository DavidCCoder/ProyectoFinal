from django import forms
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput
from django.contrib.auth.models import User 

class form_post(forms.Form):

    #Fecha= forms.DateField()
    #Autor= forms.CharField(max_length=30)
    Titulo= forms.CharField(max_length=20)
    Subtitulo= forms.CharField(max_length=40)
    Foto= forms.ImageField()
    Cuerpo= forms.CharField(
        widget=CKEditorWidget()
    )

class UserEditForm(UserCreationForm):

    username = forms.CharField(label="Modificar nombrre de usuario")
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 


    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
    #imagen_avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}