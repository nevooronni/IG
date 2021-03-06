# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, default=False, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile/images.png', upload_to='profile/'),
        ),
    ]
