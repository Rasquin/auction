# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-21 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0003_auto_20191008_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifact',
            name='age',
            field=models.IntegerField(default=2020),
        ),
    ]
