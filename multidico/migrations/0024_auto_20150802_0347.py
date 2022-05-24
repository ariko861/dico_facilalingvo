# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multidico', '0023_auto_20150628_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='learning_progress',
            field=models.CharField(max_length=1, choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced')]),
        ),
        migrations.AlterField(
            model_name='wordmodified',
            name='learning_progress',
            field=models.CharField(max_length=1, choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced')]),
        ),
    ]
