from django.shortcuts import render
from .models import hermanas, padres
from django.http import HttpResponse
from django.template import Context,Template
# Create your views here.

def Hermana1(request):
    Hermana1= hermanas(nombre='Florencia',edad=21, nacimiento="2001-3-30")
    Hermana1.save()
    texto1=f'Mi hermana {Hermana1.nombre}, tiene {Hermana1.edad} años y nació el {Hermana1.nacimiento}'
    return HttpResponse(texto1) 

def Hermana2(request):
    Hermana2= hermanas(nombre='Camila',edad="23", nacimiento="1999-2-19")
    Hermana2.save()
    texto2=f'Mi hermana {Hermana2.nombre}, tiene {Hermana2.edad} años y nació el {Hermana2.nacimiento}'
    return HttpResponse(texto2)

def Hermana3(request):
    Hermana3= hermanas(nombre='Micaela',edad="25", nacimiento="1997-3-15")
    Hermana3.save()
    texto3=f'Mi hermana {Hermana3.nombre}, tiene {Hermana3.edad} años y nació el {Hermana3.nacimiento}'
    return HttpResponse(texto3)

def Padre(request):
    padre= padres(nombre='Daniel',edad=58, nacimiento="1963-1-01")
    padre.save()
    texto4=f'Mi papa {padre.nombre}, tiene {padre.edad} años y nació el {padre.nacimiento}'
    return HttpResponse(texto4)

def madre(request):
    Madre= padres(nombre='Alejandra',edad=49, nacimiento="1974-5-14")
    Madre.save()
    texto5=f'Mi mama {Madre.nombre}, tiene {Madre.edad} años y nació el {Madre.nacimiento}'
    return HttpResponse(texto5)

def HtmlNicolas(request):

    nom="Camila"
    edad="23"
    nacimiento="19-02-1999"

    hermana1={"nombre":nom,"edad":edad,"nacimiento":nacimiento}

    mihtml=open('C:/Users/Nico/Documents/MTV_Nicolas/Plantilla/plantilla1.html')
    plantilla= Template(mihtml.read())
    mihtml.close()
    micontexto= Context(hermana1)
    documento=plantilla.render(micontexto)
    return HttpResponse(documento)
