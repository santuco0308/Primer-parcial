# Generated by Django 4.1.1 on 2022-09-21 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reto', '0004_informacionsalud_fecha_creacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informacionsalud',
            old_name='person',
            new_name='persona',
        ),
    ]
