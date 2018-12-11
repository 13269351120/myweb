# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyjobs', '0002_auto_20181209_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyjobs',
            name='use_model_focal_length',
        ),
        migrations.AddField(
            model_name='dailyjobs',
            name='camera_focal_length_type',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='dailyjobs',
            name='estimate_focal_length',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='dailyjobs',
            name='provided_focal_length',
            field=models.FloatField(default=1850.0),
        ),
    ]
