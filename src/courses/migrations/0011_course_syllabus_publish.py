# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20171130_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='syllabus_publish',
            field=models.BooleanField(default=False),
        ),
    ]
