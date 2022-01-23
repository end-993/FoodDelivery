from django.db import models


class Menu(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField()
    obrazek = models.ImageField(upload_to='menu_zdjecia/')
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    kategoria = models.ManyToManyField('Kategoria', related_name='przedmiot')

    def __str__(self):
        return self.nazwa
    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"



class Zamawianie(models.Model):
    tworzenie = models.DateTimeField(auto_now_add=True)
    cena = models.DecimalField(max_digits=7, decimal_places=2)
    przedmioty = models.ManyToManyField(
        'Menu', related_name='zamowienie', blank=True)

    def __str__(self):
        return f'Zamowienie: {self.tworzenie.strftime("%b %d %I: %M %p")}'

    class Meta:
        verbose_name = "Zamowienie"
        verbose_name_plural = "Zamowienia"