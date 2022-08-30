from django.shortcuts import render
from .models import hermanas
from django.http import HttpResponse
from django.template import context,Template,loader
# Create your views here.

def Hermana1(request):
    Hermana1= hermanas(nombre='Florencia',edad=21, nacimiento="2001-3-30")
    Hermana3= hermanas(nombre='Micaela',edad="25", nacimiento="1997-3-15")
    Hermana1.save()
    Hermana3.save()
    texto1=f'Mi hermana {Hermana1.nombre}, tiene {Hermana1.edad} años y nacio el {Hermana1.nacimiento}'
    texto3=f'Mi hermana {Hermana3.nombre}, tiene {Hermana3.edad} años y nacio el {Hermana3.nacimiento}'
    return HttpResponse(texto1)

def Hermana2(request):
    Hermana2= hermanas(nombre='Camila',edad="23", nacimiento="1999-2-19")
    Hermana2.save()
    texto2=f'Mi hermana {Hermana2.nombre}, tiene {Hermana2.edad} años y nacio el {Hermana2.nacimiento}'
    return HttpResponse(texto2)

def HtmlNicolas(request):
    nom= "Camila"
    edad= "23"
    nac= "19-02-1999"
    hermana={"nombre":nom,"edad":edad, "nacimiento":nac}
    plantilla=loader.get_template('Plantilla1.html')
    documento=plantilla.render(hermana)
    return HttpResponse(documento)