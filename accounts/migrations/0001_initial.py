# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-05 17:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
