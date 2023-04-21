from django.urls import path
from .views import *



urlpatterns = [
    path('', inicio, name='inicio'),
    path('libros/', libros, name='libros'),
    path('autores/', autores, name='autores'),
    path('bibliotecas/', bibliotecas, name='bibliotecas'),
    path('buscar/', buscar, name='buscar'),

]