# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20170227_1845'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dictionary',
            options={'ordering': ['count', 'word']},
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]