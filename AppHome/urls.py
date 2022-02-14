from django.urls import path
from AppHome import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("", views.inicio, name= 'inicio'),
    path("post", views.post, name= 'post'),
    path("CrearPost", views.crear_post, name="CrearPost"),
    


    path("pages/", views.PostList.as_view(), name = 'Lista'),
    path("pages/<pk>/", views.PostDetalle.as_view(), name = 'Detalle'),
    path("CrearPost", views.PostCreacion.as_view(), name = 'Crear'),
    path("ActualizarPost/<pk>/", views.PostUpdate.as_view(), name = 'Actualiza'),
    path("ElimnarPost/<pk>/", views.PostBorrar.as_view(), name = 'Borrar'),
    path("Perfil", views.perfil, name = 'Perfil'),
    path("InfoPerfil", views.info_perfil, name = 'InfoPerfil'),

    path("Login", views.login_request, name= 'Login'),
    path("Logout", LogoutView.as_view(template_name="AppHome/logout.html"), name = 'Logout'),
    path("Register", views.register, name= 'Register'),
    path("editarPerfil", views.editarPerfil, name= "EditarPerfil"),
    path("about", views.informacion, name= 'informacion'),

    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    path('EnviarMensaje', views.enviar_mensaje, name="EnviarMensaje"),
    path('ListaMensajes/', views.MensajeList.as_view(), name = 'ListaMensajes'),
    path("DetalleMensajes/<pk>/", views.MensajeDetalle.as_view(), name = 'DetalleMensajes'),
    path('Mensajes', views.mensajes, name = 'Mensajes'),

]