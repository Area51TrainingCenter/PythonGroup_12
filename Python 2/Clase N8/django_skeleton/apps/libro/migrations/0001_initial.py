# Generated by Django 2.0.7 on 2019-09-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro_Consultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Titulo')),
                ('author', models.CharField(max_length=200, verbose_name='Autor')),
                ('year', models.DateField(verbose_name='Año de publicacion')),
            ],
        ),
    ]
