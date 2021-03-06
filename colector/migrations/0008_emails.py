# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-01 13:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colector', '0007_auto_20200601_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colector.Station', unique=True)),
            ],
        ),
    ]
