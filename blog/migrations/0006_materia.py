# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nombre', models.TextField()),
                ('horarios', models.TextField()),
                ('dias_clase', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_inicio', models.DateTimeField(blank=True, null=True)),
                ('fecha_fin', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
