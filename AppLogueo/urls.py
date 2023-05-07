from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *



urlpatterns = [
    path('login/', login_request, name='login'),
    path('registros/', register, name='registros'),
    path('logout/', LogoutView.as_view(template_name='AppLogueo/logout.html'), name='logout'),
    path('edit-usuario/', edit_usuario, name='edit-usuario'), #raro
    path('add-avatar/', add_avatar, name='add-avatar'),
    path('accounts/login/', login_request, name='login'),

]#Listo?