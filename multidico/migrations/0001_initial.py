# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lang_name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('english', models.CharField(max_length=300)),
                ('english_local_prononciation', models.CharField(max_length=300)),
                ('french', models.CharField(max_length=300)),
                ('french_local_prononciation', models.CharField(max_length=300)),
                ('local_language', models.CharField(max_length=300)),
                ('prononciation', models.CharField(max_length=300)),
                ('category', models.ForeignKey(to='multidico.Category')),
                ('language', models.ForeignKey(to='multidico.Language')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
