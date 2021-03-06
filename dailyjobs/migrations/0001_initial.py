# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dailyjobs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('testname', models.CharField(max_length=50)),
                ('parameters', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('user', models.CharField(max_length=20)),
                ('state', models.IntegerField(default=0, editable=False)),
                ('mean_error', models.FloatField(default=-1.0, editable=False)),
                ('medium_error', models.FloatField(default=-1.0, editable=False)),
                ('time_cost', models.FloatField(default=-1.0, editable=False)),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]
