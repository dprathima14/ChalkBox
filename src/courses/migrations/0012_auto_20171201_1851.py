# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 23:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_course_syllabus_publish'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='syllabus_publish',
            new_name='publish_syllabus',
        ),
    ]
