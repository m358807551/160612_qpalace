# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-24 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_mnlp'),
    ]

    operations = [
        migrations.CreateModel(
            name='MVim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('solution', models.TextField()),
            ],
        ),
    ]
