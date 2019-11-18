# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-18 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('image', models.ImageField(upload_to='images')),
                ('origin', models.CharField(default='', max_length=200)),
                ('year', models.IntegerField(default=2020)),
                ('description', models.TextField()),
                ('crafting', models.TextField()),
                ('trajectory', models.TextField()),
                ('by_user', models.CharField(default='', max_length=100)),
                ('expert_value', models.DecimalField(decimal_places=2, max_digits=9)),
                ('current_bidding_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('buy_now_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('price_to_pay', models.DecimalField(decimal_places=2, max_digits=9)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('bidding_time', models.DurationField(null=True)),
                ('on_bidding', models.BooleanField(default=True)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]
