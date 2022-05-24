# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multidico', '0024_auto_20150802_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='learning_progress',
            field=models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced'), ('F', 'Fluent'), ('S', 'Slang')], max_length=1),
        ),
        migrations.AlterField(
            model_name='wordmodified',
            name='learning_progress',
            field=models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced'), ('F', 'Fluent'), ('S', 'Slang')], max_length=1),
        ),
    ]
