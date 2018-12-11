# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_auto_20181209_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='use_model_focal_length',
        ),
        migrations.AddField(
            model_name='post',
            name='camera_focal_length_type',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='post',
            name='estimate_focal_length',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='provided_focal_length',
            field=models.FloatField(default=1850.0),
        ),
    ]
