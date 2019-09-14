# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from os.path import dirname, abspath, join

from django.db import migrations, models
import django.db.models.deletion


def create_ubigeos(apps, schema_editor):
    Ubigeo = apps.get_model('ubigeo', 'Ubigeo')
    with open(join(dirname(abspath(__file__)), 'initial_data.json')) as f:
        for item in json.loads(f.read()):
            Ubigeo.objects.create(**item)


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Ubigeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(
                    blank=True, null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to='ubigeo.Ubigeo')),
            ],
        ),
        migrations.RunPython(create_ubigeos),
    ]

