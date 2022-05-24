# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multidico', '0008_auto_20150604_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='I_want_to_learn_english',
            field=models.CharField(max_length=400, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='language',
            name='I_want_to_learn_french',
            field=models.CharField(max_length=400, null=True, blank=True),
            preserve_default=True,
        ),
    ]
