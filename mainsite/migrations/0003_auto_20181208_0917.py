# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20181208_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mean_error',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='post',
            name='medium_error',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='post',
            name='time_cost',
            field=models.FloatField(default=-1.0),
        ),
    ]
