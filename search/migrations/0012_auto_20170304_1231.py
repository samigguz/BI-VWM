# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 12:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0011_item_count_of_terms'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dictionary',
            options={'ordering': ['-weight', 'word']},
        ),
    ]
