from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppHome.models import Post, Avatar, User, Mensajeria
from AppHome.forms import form_post, UserEditForm, UserRegisterForm, AvatarFormulario, form_mensajeria
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin

@login_required
def inicio(request):

    avatares = Avatar.objects.filter(user=request.user.id)

    return render(request, 'AppHome/inicio.html', {"url":avatares[0].imagen.url})

def padre(request):

    return render(request, 'AppHome/padre.html')

def mensajes(request):

    if request.user.is_authenticated and request.user.is_staff: 

        return render(request, 'AppHome/mensajes.html')
    
    else:

        return render(request, 'AppHome/errorMensaje.html')

def post(request):

    return render(request, 'AppHome/post.html')    

def informacion(request):

    return render(request, 'AppHome/informacion.html')

@login_required
def crear_post(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            FormularioPost = form_post(request.POST,files=request.FILES)
            print(FormularioPost)
            if FormularioPost.is_valid():
                info = FormularioPost.cleaned_data
                post = Post(Fecha=Post.Fecha, Autor=request.user,Titulo=info['Titulo'],Subtitulo=info['Subtitulo'],Foto=info['Foto'], Cuerpo=info['Cuerpo'], Equipo=info['Equipo'])
                post.save()
                #return render(request, "AppHome/inicio.html")
                return redirect('post')
            else:
                #algo mal en el formulario
                return render(request, "AppHome/inicio.html",{"mensaje":"Error, datos incorrectos"})

        else:
            #no esta logueado
            return render(request, "AppHome/inicio.html",{"mensaje":"Error, no esta logueado"})
    else: 
        FormularioPost= form_post()
    return render(request, "AppHome/CrearPost.html", {"FormularioPost":FormularioPost})

class PostList(ListView):

    model = Post
    template_name = "AppHome/ListaPost.html"

class PostDetalle(DetailView):

    model = Post
    template_name = "AppHome/DetallePost.html"

class PostCreacion(CreateView):

    model = Post
    success_url = "/AppHome/pages/"
    fields = ['titulo', 'subtitulo']

class PostUpdate(UserPassesTestMixin,UpdateView):
    
    model = Post
    success_url = "/AppHome/pages/"
    #form_class = form_post
    fields = ['Titulo', 'Subtitulo', 'Cuerpo', 'Foto']

    def test_func(self):
        post=Post.objects.get(id=self.kwargs["pk"])
        return(self.request.user.is_authenticated and (self.request.user.id == post.Autor.id or self.request.user.is_staff))


class PostBorrar(UserPassesTestMixin,DeleteView):

    model = Post
    success_url = "/AppHome/pages/"
    template_name = "AppHome/post.confirm.delete.html"

    def test_func(self):
        post=Post.objects.get(id=self.kwargs["pk"])
        return(self.request.user.is_authenticated and (self.request.user.id == post.Autor.id or self.request.user.is_staff))

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return redirect('inicio')

            else:

                return render(request,"AppHome/inicio.html", {"mensaje":"Error, los datos son incorrectos"})

        else:

            return render(request,"AppHome/inicio.html", {"mensaje":"Error, los datos ingresados son incorrectos"})
    else:

        form = AuthenticationForm()

        return render(request, "AppHome/login.html", {'form':form})


def register(request):

    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('AgregarAvatar')

    else:

        form = UserRegisterForm()

    return render(request, "AppHome/registro.html", {"form":form})

@login_required
def editarPerfil(request):
 
      usuario = request.user
     
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST) 
            if miFormulario.is_valid():   

                  informacion = miFormulario.cleaned_data

                  usuario.username = informacion['username']
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password1']
                  usuario.save()

                  return redirect("inicio") 
      
      else: 
            
            miFormulario= UserEditForm(initial={ 'email':usuario.email}) 

      return render(request, "AppHome/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})


@login_required
def agregarAvatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES) 

            if miFormulario.is_valid():   


                  u = User.objects.get(username=request.user)
                
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return redirect('inicio')

      else: 

            miFormulario= AvatarFormulario() 

      return render(request, "AppHome/agregarAvatar.html", {"miFormulario":miFormulario})

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            FormularioMensaje = form_mensajeria(request.POST)
            #print(FormularioMensaje)
            if FormularioMensaje.is_valid():
                datos = FormularioMensaje.cleaned_data
                mensaje = Mensajeria(Fecha=Mensajeria.Fecha, Autor=request.user,Asunto=datos['Asunto'],Mensaje=datos['Mensaje'])
                mensaje.save()
                return redirect('inicio')
            else:
                return render(request, "AppHome/inicio.html",{"mensaje":"Error, datos incorrectos"})

        else:
            return render(request, "AppHome/inicio.html",{"mensaje":"Error, no esta logueado"})
    else: 
        FormularioMensaje= form_mensajeria()
    return render(request, "AppHome/enviarMensaje.html", {"FormularioMensaje":FormularioMensaje})

class MensajeList(ListView):

    model = Mensajeria
    template_name = "AppHome/ListaMensajes.html"


class MensajeDetalle(DetailView):

    model = Mensajeria
    template_name = "AppHome/DetalleMensajes.html"


def perfil(request):

    return render(request, 'AppHome/perfil.html')

def info_perfil(request):

    avatares = Avatar.objects.filter(user=request.user.id)

    return render(request, 'AppHome/InfoPerfil.html', {"url":avatares[0].imagen.url})