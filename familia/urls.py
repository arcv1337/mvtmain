from django.urls import path
from familia import views


urlpatterns = [
    path('', views.index, name="index"),
    path('agregar/', views.agregar, name="agregar"),
    path('buscar/', views.buscar, name="buscar"),
    path('borrar/<identificador>', views.borrar, name="borrar"),
]
