from django.shortcuts import render

#from django.template import Template, Context, loader
from AppProyecto.models import *
from .forms import *


def inicio (request):
    return render(request,'AppProyecto/inicio.html')

def libros (request):
    mis_libros=libro.objects.all()

    if request.method == 'POST':
        mi_formu = LibrosFormulario(request.POST)

        if mi_formu.is_valid():
            informacion = mi_formu.cleaned_data
            librodb= libro(titulo=informacion['titulo'], editorial=informacion['editorial'], paginas=informacion['paginas'])
            librodb.save()
            nuevo_libro = {'titulo': informacion['titulo'], 'editorial':informacion['editorial'], 'paginas':informacion['paginas']}
            return render (request, 'AppProyecto/libros.html',{'librosformulario': mi_formu, 'nuevo_libro':nuevo_libro,"mis_libros":mis_libros })
    else:
        mi_formu=LibrosFormulario()

    return render(request,'AppProyecto/libros.html', {'librosformulario':mi_formu,'mis_libros':mis_libros})




def autores (request):
    mis_autores=autor.objects.all()


    if request.method == 'POST':
        mi_formu = AutoresFormulario(request.POST)

        if mi_formu.is_valid():
            informacion = mi_formu.cleaned_data
            autordb= autor(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'])
            autordb.save()
            nuevo_autor={'nombre': informacion['nombre'], 'apellido':informacion['apellido'], 'edad':informacion['edad']}
            return render (request, 'AppProyecto/autores.html',{'autoresformulario': mi_formu,'nuevo_autor':nuevo_autor,"mis_autores":mis_autores})
    else:
        mi_formu=AutoresFormulario()
    return render(request, 'AppProyecto/autores.html', {'autoresformulario':mi_formu, 'mis_autores':mis_autores})


def bibliotecas (request):
    mis_bibliotecas = biblioteca.objects.all()

    if request.method == 'POST':
        mi_formu = BibliotecasFormulario(request.POST)

        if mi_formu.is_valid():
            informacion = mi_formu.cleaned_data
            bibliotecadb= biblioteca(nombre=informacion['nombre'], direccion=informacion['direccion'], email=informacion['email'])
            bibliotecadb.save()
            nueva_biblioteca={'nombre': informacion['nombre'], 'direccion':informacion['direccion'], 'email':informacion['email']}
            return render (request, 'AppProyecto/bibliotecas.html',{'bibliotecasformulario': mi_formu,'nueva_biblioteca':nueva_biblioteca,"mis_bibliotecas":mis_bibliotecas})
    else:
        mi_formu=BibliotecasFormulario()
    return render(request, 'AppProyecto/bibliotecas.html',{'bibliotecasformulario':mi_formu, 'mis_bibliotecas':mis_bibliotecas})
      

def buscar(request):
    if request.GET["editorial"]:
        edi= request.GET["editorial"]
        resultado=libro.objects.filter(editorial__icontains = edi)

        return render (request, 'AppProyecto/inicio.html',{'Libros':resultado, 'Editorial':edi})
    else:
        respuesta='no se encontraron libros de esa editorial'
    return render(request, 'AppProyecto/inicio.html',{'respuesta':respuesta})



# def saludar(request):
#     return HttpResponse("!hola mundo!")


#def probandoHtml(request):

   # diccionario={"nombre":"Nacho", "apellido": "Suarez", "edad":25}

    # archivo=open(r"C:\Users\isuarez\python2\Tercera pre-entrega Suarez\Terceratp\Plantillas\template1.html")

    # template=Template(archivo.read())
    # archivo.close()
    
    # contexto=Context(diccionario)
    # documento=template.render(contexto)
      

   # return HttpResponse(documento)





# def probandoHtml(request):  

#     diccionario={"nombre":"Nacho", "apellido": "Suarez", "edad":25}

#     template=loader.get_template("template1.html")

#     documento=template.render(diccionario)

#     return HttpResponse(documento)


# def cargar_libro(request):
    
#     titulo_libro="La Metamorfosis"
#     nombre_editorial="Kurt Wolff Verlag"
#     cantidad_paginas=80

#     libro=Libro(titulo=titulo_libro, editorial=nombre_editorial, paginas=cantidad_paginas)
#     libro.save()

#     respuesta=f"se a cargado el libro: {titulo_libro}"

#     return HttpResponse(respuesta)

