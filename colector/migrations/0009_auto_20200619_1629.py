# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-19 13:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colector', '0008_emails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emails',
            options={'verbose_name_plural': 'Email'},
        ),
    ]