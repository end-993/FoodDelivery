# Generated by Django 4.0.1 on 2022-01-23 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restauracja', '0009_rename_zamowienie_zamawianie'),
    ]

    operations = [
        migrations.AddField(
            model_name='zamawianie',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='zamawianie',
            name='imie',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='zamawianie',
            name='kod_pocztowy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='zamawianie',
            name='miasto',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='zamawianie',
            name='ulica',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
