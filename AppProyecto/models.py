from django.db import models

# Create your models here.

class libro(models.Model):
    titulo=models.CharField(max_length=50)
    editorial=models.CharField(max_length=50)
    paginas=models.IntegerField()
    portada=models.ImageField(upload_to='libro',null=True,blank=True, default='blank.png')
    review=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.titulo+ "de" + self.editorial 
    
    
class biblioteca(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    foto=models.ImageField(upload_to='biblioteca',null=True,blank=True, default='blank.png')
    biografia=models.TextField(null=True,blank=True) #cambiarrrr
     
    def __str__(self):
        return self.nombre
    

class autor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.CharField(max_length=50)
    foto=models.ImageField(upload_to='autor',null=True,blank=True,default='blank.png')
    biografia=models.TextField(null=True,blank=True)   

    def __str__(self):
        return self.nombre + self.apellido
    
    class meta:
        verbose_name_plural='Autores'

        

#Listo

class mensaje(models.Model):

   
    mensaje=models.CharField(max_length=250)

    def __str__(self):
        return  self.mensaje 
    
