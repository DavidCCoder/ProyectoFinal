from django.shortcuts import render
from django.http import HttpResponse
from AppHome.models import Post
from AppHome.forms import form_post

# Create your views here.

def ver_post(request):

    posts= Post.objects.all()

    return render(request, 'AppHome/VerPost.html',{"posts":posts})

def inicio(request):

    return render(request, 'AppHome/inicio.html')

def padre(request):

    return render(request, 'AppHome/padre.html')

def post(request):

    return render(request, 'AppHome/post.html')

def crear_post(request):

    if request.method == 'POST':

        FormularioPost = form_post(request.POST)

        print(FormularioPost)

        if FormularioPost.is_valid:

            info = FormularioPost.cleaned_data

            post = Post(Fecha=info['Fecha'],Autor=info['Autor'],Titulo=info['Titulo'],Subtitulo=info['Subtitulo'],Cuerpo=info['Cuerpo'])

            post.save()

            return render(request, "AppHome/inicio.html")

    else: 

        FormularioPost= form_post()

    return render(request, "AppHome/CrearPost.html", {"FormularioPost":FormularioPost})


