# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-30 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocplus', '0011_auto_20180629_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlearninglanguage',
            name='classification',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
