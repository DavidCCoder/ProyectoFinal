from django.urls import path
from AppHome import views

urlpatterns = [

    path("", views.inicio, name= 'inicio'),
    path("post", views.post, name= 'post'),
    path("CrearPost", views.crear_post, name="CrearPost"),
    path("VerPost/", views.ver_post, name="VerPost"),
   
]