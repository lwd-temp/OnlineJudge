# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0003_userprofile_total_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='problems_status',
            new_name='acm_problems_status',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='oi_problems_status',
            field=jsonfield.fields.JSONField(default={}),
        ),
        migrations.RemoveField(
            model_name='user',
            name='real_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='student_id',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='real_name',
            field=models.CharField(max_length=30, blank=True, null=True),
        ),
    ]
