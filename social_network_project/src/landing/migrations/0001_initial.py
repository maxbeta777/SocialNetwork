# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'MyGuest',
                'verbose_name_plural': 'A lot of Guests',
            },
        ),
    ]