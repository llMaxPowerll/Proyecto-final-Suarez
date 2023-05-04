from django.urls import path
from .views import *



urlpatterns = [
    path('', inicio, name='inicio'),
    #path('libros/', libros, name='libros'),
    #path('autores/', autores, name='autores'),
    #path('bibliotecas/', bibliotecas, name='bibliotecas'),
    path('buscar/', buscar, name='buscar'),

    path('add-libro/', Add_libro.as_view(), name='add-libro'),
    path('reed-libros/', Reed_libro.as_view(), name='reed-libros'),
    path('delete-libro/<pk>', Delete_libro.as_view(),name='delete-libro'),
    path('update-libro/<pk>', Update_libro.as_view(),name='update-libro'),
    path('detail-libro/<pk>',Detail_libro.as_view(), name='detail-libro'),

    path('list-autor/',List_autor.as_view(), name='list-autor'),
    path('detail-autor/<pk>',Detail_autor.as_view(), name='detail-autor'),
    path('create-autor/',Create_autor.as_view(), name='create-autor'),
    path('update-autor/<pk>',Update_autor.as_view(), name='update-autor'),
    path('delete-autor/<pk>',Delete_autor.as_view(), name='delete-autor'),

    path('list-biblioteca/',List_biblioteca.as_view(), name='list-biblioteca'),
    path('detail-biblioteca/<pk>',Detail_biblioteca.as_view(), name='detail-biblioteca'),
    path('create-biblioteca/',Create_biblioteca.as_view(), name='create-biblioteca'),
    path('update-biblioteca/<pk>',Update_biblioteca.as_view(), name='update-biblioteca'),
    path('delete-biblioteca/<pk>',Delete_biblioteca.as_view(), name='delete-biblioteca'),



]