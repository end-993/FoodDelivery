from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from django.shortcuts import render
from django.views import View
from .models import *


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class Onas(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'onas.html')


class Zamowienie(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        zupy = Menu.objects.filter(kategoria__nazwa__contains='Zupy')
        dania_glowne = Menu.objects.filter(kategoria__nazwa__contains='Dania główne')
        pizza = Menu.objects.filter(kategoria__nazwa__contains='Pizza')
        napoje = Menu.objects.filter(kategoria__nazwa__contains='Napoje')


        context = {
            'zupy': zupy,
            'dania_glowne': dania_glowne,
            'pizza': pizza,
            'napoje': napoje,
        }

        # render the template
        return render(request, 'zamowienie.html', context)

    def post(self, request, *args, **kwargs):
        zamowione_przedmioty = {
            'przedmioty': []
        }

        przedmioty = request.POST.getlist('przedmioty[]')

        for przedmiot in przedmioty:
            menu = Menu.objects.get(pk__contains=int(przedmiot))
            przedmiot_data = {
                'id': menu.pk,
                'nazwa': menu.nazwa,
                'cena': menu.cena
            }

            zamowione_przedmioty['przedmioty'].append(przedmiot_data)

            cena = 0
            przedmiot_ids = []

        for przedmiot in zamowione_przedmioty['przedmioty']:
            cena += przedmiot['cena']
            przedmiot_ids.append(przedmiot['id'])

        zamowienie = Zamawianie.objects.create(cena=cena)
        zamowienie.przedmioty.add(*przedmiot_ids)

        context = {
            'przedmioty': zamowione_przedmioty['przedmioty'],
            'cena': cena
        }

        return render(request, 'zamowienie_potwierdzenie.html', context)


