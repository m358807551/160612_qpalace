# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-15 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_mgit'),
    ]

    operations = [
        migrations.CreateModel(
            name='MHtml',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('solution', models.TextField()),
            ],
        ),
    ]
