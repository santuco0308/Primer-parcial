# Generated by Django 4.1.1 on 2022-09-21 18:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reto', '0003_rename_person_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='informacionsalud',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
