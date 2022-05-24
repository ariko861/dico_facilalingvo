# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multidico', '0015_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='subcategory',
            field=models.ForeignKey(blank=True, to='multidico.SubCategory', null=True),
            preserve_default=True,
        ),
    ]
