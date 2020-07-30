# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-01 13:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colector', '0005_auto_20200409_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_mail', models.CharField(max_length=128)),
                ('nd_mail', models.CharField(max_length=128)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colector.Station', unique=True)),
            ],
        ),
    ]