# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-23 07:59
from __future__ import unicode_literals

import django.db.models.deletion
import jsonfield.fields
from django.conf import settings
from django.db import migrations, models

import account.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                (
                    'last_login',
                    models.DateTimeField(
                        blank=True, null=True, verbose_name='last login'
                    ),
                ),
                ('username', models.CharField(max_length=30, unique=True)),
                ('real_name', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('admin_type', models.CharField(default='regular_user', max_length=24)),
                ('reset_password_token', models.CharField(max_length=40, null=True)),
                ('reset_password_token_expire_time', models.DateTimeField(null=True)),
                ('auth_token', models.CharField(max_length=40, null=True)),
                ('two_factor_auth', models.BooleanField(default=False)),
                ('tfa_token', models.CharField(max_length=40, null=True)),
                ('open_api', models.BooleanField(default=False)),
                ('open_api_appkey', models.CharField(max_length=35, null=True)),
                ('is_disabled', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', account.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('problems_status', jsonfield.fields.JSONField(default={})),
                ('avatar', models.CharField(default='default.png', max_length=50)),
                ('blog', models.URLField(blank=True, null=True)),
                ('mood', models.CharField(blank=True, max_length=200, null=True)),
                ('accepted_problem_number', models.IntegerField(default=0)),
                ('submission_number', models.IntegerField(default=0)),
                (
                    'phone_number',
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                ('school', models.CharField(blank=True, max_length=200, null=True)),
                ('major', models.CharField(blank=True, max_length=200, null=True)),
                ('student_id', models.CharField(blank=True, max_length=15, null=True)),
                ('time_zone', models.CharField(blank=True, max_length=32, null=True)),
                ('language', models.CharField(blank=True, max_length=32, null=True)),
                (
                    'user',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'db_table': 'user_profile',
            },
        ),
    ]
