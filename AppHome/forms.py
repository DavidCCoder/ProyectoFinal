from django import forms
from ckeditor.widgets import CKEditorWidget

class form_post(forms.Form):

    Fecha= forms.DateField()
    Autor= forms.CharField(max_length=30)
    Titulo= forms.CharField(max_length=20)
    Subtitulo= forms.CharField(max_length=40)
    Foto= forms.ImageField()
    Cuerpo= forms.CharField(
        widget=CKEditorWidget()
    )