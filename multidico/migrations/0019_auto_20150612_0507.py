# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multidico', '0018_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='digit',
            field=models.DecimalField(default=0, max_digits=19, decimal_places=10),
            preserve_default=True,
        ),
    ]
