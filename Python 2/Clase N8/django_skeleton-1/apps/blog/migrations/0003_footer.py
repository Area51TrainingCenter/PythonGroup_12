# Generated by Django 2.0.7 on 2019-10-05 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191005_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripción')),
            ],
        ),
    ]