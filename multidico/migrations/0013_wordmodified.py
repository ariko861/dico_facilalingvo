# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('multidico', '0012_auto_20150609_0831'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordModified',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('learning_progress', models.CharField(max_length=1, choices=[(b'B', b'Beginner'), (b'I', b'Intermediate'), (b'A', b'Advanced')])),
                ('english', models.CharField(max_length=300)),
                ('english_local_prononciation', models.CharField(max_length=300)),
                ('french', models.CharField(max_length=300)),
                ('french_local_prononciation', models.CharField(max_length=300)),
                ('local', models.CharField(max_length=300)),
                ('prononciation', models.CharField(max_length=300, null=True, blank=True)),
                ('category', models.ForeignKey(to='multidico.Category')),
                ('language', models.ForeignKey(to='multidico.Language')),
                ('modifier', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('word_origin', models.ForeignKey(to='multidico.Word')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
