# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-30 14:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_articleword_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articleword',
            old_name='total',
            new_name='position',
        ),
    ]
