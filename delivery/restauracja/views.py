from django.core.mail import send_mail

from django.shortcuts import render
from django.views import View
from .models import *

from django.shortcuts import render, redirect
from django.views import View
from django.utils.timezone import datetime
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import Q


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
        imie = request.POST.get('imie')
        email = request.POST.get('email')
        ulica = request.POST.get('ulica')
        miasto = request.POST.get('miasto')
        kod_pocztowy = request.POST.get('kod_pocztowy')
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

        zamowienie = Zamawianie.objects.create(
            cena=cena,
            imie=imie,
            email=email,
            ulica=ulica,
            miasto=miasto,
            kod_pocztowy=kod_pocztowy
        )
        zamowienie.przedmioty.add(*przedmiot_ids)

        #Po wszytskim wyślij maila
        mail_gl = ('Dziękujemy za zamówienie! Twoje zamówienie jest w trakcie przygotowania i wkrótce zostanie dostarczone.')

        send_mail(
            'Dziękujemy za zamówienie!',
            mail_gl,
            'przyklad@przyklad.com',
            [email],
            fail_silently=False
        )

        context = {
            'przedmioty': zamowione_przedmioty['przedmioty'],
            'cena': cena
        }

        return render(request, 'zamowienie_potwierdzenie.html', context)


class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        today = datetime.today()
        orders = Zamawianie.objects.filter(tworzenie__year=today.year,
                                           tworzenie__month=today.month, tworzenie__day=today.day)
        total_revenue = 0

        for order in orders:
            total_revenue += order.cena

        context = {
            'orders': orders,
            'total_revenue': total_revenue,
            'total_orders': len(orders)
        }
        return render(request, 'dashboard.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Personel').exists()


class MenuDania(View):
    def get(self, request, *args, **kwargs):
        dania = Menu.objects.all()

        context = {
            'dania': dania,
        }

        return render(request, 'menu.html', context)

class MenuSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")

        dania = Menu.objects.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query)
        )

        context = {
            'dania': dania
        }
        return render(request, 'menu.html', context)