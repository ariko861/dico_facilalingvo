# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multidico', '0014_auto_20150609_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subcategory_name', models.CharField(max_length=200)),
                ('subcategory_french_name', models.CharField(max_length=200, null=True, blank=True)),
                ('order_index', models.IntegerField(default=100)),
                ('parent', models.ForeignKey(to='multidico.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
