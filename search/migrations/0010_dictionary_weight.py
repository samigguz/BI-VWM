# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0009_word_idf'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionary',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
