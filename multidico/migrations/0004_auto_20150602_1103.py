# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multidico', '0003_auto_20150602_1027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='language',
            old_name='language_text',
            new_name='language_name',
        ),
    ]
