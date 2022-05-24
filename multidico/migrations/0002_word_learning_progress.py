# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multidico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='learning_progress',
            field=models.CharField(default='B', max_length=1, choices=[(b'B', b'Beginner'), (b'I', b'Intermediate'), (b'A', b'Advanced')]),
            preserve_default=False,
        ),
    ]
