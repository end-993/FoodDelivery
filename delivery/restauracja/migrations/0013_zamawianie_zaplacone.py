# Generated by Django 4.0.1 on 2022-01-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restauracja', '0012_alter_zamawianie_kod_pocztowy'),
    ]

    operations = [
        migrations.AddField(
            model_name='zamawianie',
            name='zaplacone',
            field=models.BooleanField(default=False),
        ),
    ]
