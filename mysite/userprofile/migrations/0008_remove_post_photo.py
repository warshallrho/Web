# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 12:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_post_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
    ]
