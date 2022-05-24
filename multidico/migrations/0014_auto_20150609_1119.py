# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multidico', '0013_wordmodified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordmodified',
            name='word_origin',
            field=models.ForeignKey(blank=True, to='multidico.Word', null=True),
            preserve_default=True,
        ),
    ]
