# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20171129_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default=False, upload_to='profile/'),
        ),
    ]
