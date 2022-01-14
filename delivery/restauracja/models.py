from django.db import models

# Create your models here.


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa + " "

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

class Dania(models.Model):
    nazwa = models.CharField(max_length = 100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12,decimal_places=2)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(null=True,blank=True)


    def __str__(self):
        return self.nazwa +" "
    class Meta:
        verbose_name = "Danie"
        verbose_name_plural = "Dania"