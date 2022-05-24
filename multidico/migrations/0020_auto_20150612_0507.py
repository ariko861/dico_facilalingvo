# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multidico', '0019_auto_20150612_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='digit',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
