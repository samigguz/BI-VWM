# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0010_dictionary_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='count_of_terms',
            field=models.IntegerField(default=0),
        ),
    ]
