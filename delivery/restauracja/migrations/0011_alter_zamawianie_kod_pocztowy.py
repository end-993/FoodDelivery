# Generated by Django 4.0.1 on 2022-01-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restauracja', '0010_zamawianie_email_zamawianie_imie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zamawianie',
            name='kod_pocztowy',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]