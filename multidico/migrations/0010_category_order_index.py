# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multidico', '0009_auto_20150607_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order_index',
            field=models.IntegerField(default=100),
            preserve_default=True,
        ),
    ]
