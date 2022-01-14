from django.shortcuts import render
from django.http import HttpResponse
from .models import Kategoria,Dania
# Create your views here.
def index(request):
   # wszystkie = produkty.objects.all()
   # jeden = produkty.objects.get(pk=2)
   # nazwa_kat = kategoria.objects.all()
   # null = produkty.objects.filter(kategoria__isnull=False)
    #zawiera = produkty.objects.filter(opis__icortains='dysk')
    kategorie = Kategoria.objects.all()
    dane = {'kategorie' : kategorie}
    return render(request,'index.html',dane)
def onas(request):
    kategorie = Kategoria.objects.all()
    dane = {'kategorie': kategorie}
    return render(request,'onas.html',dane)

def kategoria(request,id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_danie = Dania.objects.filter(kategoria = kategoria_user)
    kategorie = Kategoria.objects.all()
    dane =   {'kategoria_user' : kategoria_user,
              'kategoria_danie' : kategoria_danie,
              'kategorie' : kategorie}
    return render(request,'kategoria_danie.html',dane)

def danie(request,id):
    danie_user = Dania.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    dane = {'danie_user' : danie_user, 'kategorie' : kategorie}
    return render(request,'danie.html',dane)



