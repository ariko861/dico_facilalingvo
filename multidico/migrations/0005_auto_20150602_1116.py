# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multidico', '0004_auto_20150602_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='prononciation',
            field=models.CharField(max_length=300, null=True),
            preserve_default=True,
        ),
    ]
