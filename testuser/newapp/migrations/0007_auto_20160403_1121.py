# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0006_auto_20160403_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='date_of_complaint',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='description',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 4, 3, 5, 51, 51, 861889, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='students',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]