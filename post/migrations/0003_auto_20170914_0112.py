# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20170911_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(verbose_name='Выдержка'),
        ),
    ]