# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0006_auto_20170928_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.CharField(blank=True, max_length=128, verbose_name='address'),
        ),
    ]