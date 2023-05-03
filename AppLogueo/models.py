from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Avatar (models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    imagen=models.ImageField(upload_to='avatars',default='blank.png')
    def __str__(self):
        return self.user.username
    
#Listo
