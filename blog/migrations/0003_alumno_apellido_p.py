# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alumno'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='apellido_p',
            field=models.CharField(default=datetime.datetime(2017, 4, 13, 12, 47, 20, 484375, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
