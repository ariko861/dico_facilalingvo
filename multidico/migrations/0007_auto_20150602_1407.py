# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multidico', '0006_auto_20150602_1207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='local_language',
            new_name='local',
        ),
    ]
