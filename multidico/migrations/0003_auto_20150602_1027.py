# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multidico', '0002_word_learning_progress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='language',
            old_name='lang_name',
            new_name='language_text',
        ),
    ]
