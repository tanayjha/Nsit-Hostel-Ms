# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-28 17:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_auto_20160328_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 28, 17, 43, 20, 535445, tzinfo=utc)),
        ),
    ]