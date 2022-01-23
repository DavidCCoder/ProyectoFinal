from django.shortcuts import render
from django.http import HttpResponse
from AppHome.models import Post
from AppHome.forms import form_post
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
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


class PostList(ListView):

    model = Post
    template_name = "AppHome/ListaPost.html"

class PostDetalle(DeleteView):

    model = Post
    template_name = "AppHome/DetallePost.html"

class PostCreacion(CreateView):

    model = Post
    success_url = "/AppHome/ListaPost"
    fields = ['titulo', 'subtitulo']

class PostUpdate(UpdateView):

    model = Post
    success_url = "/AppHome/ListaPost"
    fields = ['Titulo', 'Subtitulo', 'Autor', 'Cuerpo']

class PostBorrar(DeleteView):

    model = Post
    success_url = "/AppHome/ListaPost"
    template_name = "AppHome/post.confirm.delete.html"

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request,"AppHome/inicio.html", {"mensaje":f"Bienvenido {usuario}"})

            else:

                return render(request,"AppHome/inicio.html", {"mensaje":"Error, los datos son incorrectos"})

        else:

            return render(request,"AppHome/inicio.html", {"mensaje":"Error, formulario erroneo"})
    else:

        form = AuthenticationForm()

        return render(request, "AppHome/login.html", {'form':form})


def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppHome/inicio.html", {"mensaje":"Usuario creado correctamente"})

    else:

        form = UserCreationForm()

    return render(request, "AppHome/registro.html", {"form":form})