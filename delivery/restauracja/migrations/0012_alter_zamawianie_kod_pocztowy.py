# Generated by Django 4.0.1 on 2022-01-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restauracja', '0011_alter_zamawianie_kod_pocztowy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zamawianie',
            name='kod_pocztowy',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
