# Generated by Django 4.1.1 on 2022-09-21 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reto', '0002_rename_task_informacionsalud'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Persona',
        ),
    ]
