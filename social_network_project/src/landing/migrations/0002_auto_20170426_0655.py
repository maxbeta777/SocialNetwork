# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 03:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guest',
            options={'verbose_name': 'Guest', 'verbose_name_plural': 'Guests'},
        ),
    ]
