from django.urls import path
from AppHome import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("", views.inicio, name= 'inicio'),
    path("post", views.post, name= 'post'),
    path("CrearPost", views.crear_post, name="CrearPost"),


    path("ListaPost/", views.PostList.as_view(), name = 'Lista'),
    path("DetallePost/<pk>/", views.PostDetalle.as_view(), name = 'Detalle'),
    path("CrearPost", views.PostCreacion.as_view(), name = 'Crear'),
    path("ActualizarPost/<pk>/", views.PostUpdate.as_view(), name = 'Actualiza'),
    path("ElimnarPost/<pk>/", views.PostBorrar.as_view(), name = 'Borrar'),


    path("Login", views.login_request, name= 'Login'),
    path("Logout", LogoutView.as_view(template_name="AppHome/logout.html"), name = 'Logout'),
    path("Register", views.register, name= 'Register'),
    path("editarPerfil", views.editarPerfil, name= "EditarPerfil"),

   
]