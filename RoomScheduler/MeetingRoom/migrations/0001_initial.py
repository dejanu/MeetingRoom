# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-04 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('capacity', models.IntegerField(default=1)),
                ('status', models.BooleanField(default=False)),
                ('description', models.TextField()),
            ],
        ),
    ]