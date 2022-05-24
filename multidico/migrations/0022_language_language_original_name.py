# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multidico', '0021_auto_20150612_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='language_original_name',
            field=models.CharField(default='try', max_length=100),
            preserve_default=False,
        ),
    ]
