# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 21:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_auto_20170227_2117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dictionary',
            options={'ordering': ['-count', 'word']},
        ),
    ]
