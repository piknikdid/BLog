# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='title',
            field=models.TextField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]