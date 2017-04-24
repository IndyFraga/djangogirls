# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alumno_apellido_p'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='title',
            field=models.CharField(default=datetime.datetime(2017, 4, 13, 13, 0, 26, 937500, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='apellido_p',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.TextField(),
        ),
    ]
