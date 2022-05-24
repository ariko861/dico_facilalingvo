# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multidico', '0017_wordmodified_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('digit', models.IntegerField(null=True, blank=True)),
                ('english', models.CharField(max_length=50)),
                ('english_local_prononciation', models.CharField(max_length=50)),
                ('french', models.CharField(max_length=50)),
                ('french_local_prononciation', models.CharField(max_length=50)),
                ('local', models.CharField(max_length=50)),
                ('prononciation', models.CharField(max_length=50, null=True, blank=True)),
                ('language', models.ForeignKey(to='multidico.Language')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
