# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-09 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colector', '0004_onlinestations'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_get', models.BooleanField(default=False)),
                ('out1', models.IntegerField(default=0)),
                ('out2', models.IntegerField(default=0)),
                ('out3', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=128)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colector.Station', unique=True)),
            ],
            options={
                'verbose_name_plural': 'New Config',
            },
        ),
        migrations.AlterModelOptions(
            name='onlinestations',
            options={'verbose_name_plural': 'OnlineStatitions'},
        ),
        migrations.AlterField(
            model_name='onlinestations',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colector.Station', unique=True),
        ),
    ]