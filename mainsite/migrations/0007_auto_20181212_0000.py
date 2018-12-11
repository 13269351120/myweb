# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_auto_20181211_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bin',
            field=models.CharField(max_length=200, default='/home/luban/jincheng_test/colmap/build/src/exe/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='database_path',
            field=models.CharField(max_length=500, default='/nfs/project/daily_3drecon/20181122/3drecon/databases/samsung_starneto_1fps/database.db'),
        ),
        migrations.AlterField(
            model_name='post',
            name='geo_verify_type',
            field=models.CharField(max_length=50, default='neither'),
        ),
        migrations.AlterField(
            model_name='post',
            name='index_path',
            field=models.CharField(max_length=500, default='/nfs/project/localization/faissindex/index_trained_SoftwareParkOne20180510_trained_NoPopulate.faissindex'),
        ),
        migrations.AlterField(
            model_name='post',
            name='index_type',
            field=models.CharField(max_length=20, default='faiss'),
        ),
        migrations.AlterField(
            model_name='post',
            name='model_path',
            field=models.CharField(max_length=500, default='/nfs/project/daily_3drecon/20181122/3drecon/test_partial_ba/samsung_starneto_1fps/sparse'),
        ),
        migrations.AlterField(
            model_name='post',
            name='perf_test_images',
            field=models.CharField(max_length=500, default='/nfs/project/localization/measure_set/software_park_two/20181129_samsung_test_1fps_00_01_filtered.txt'),
        ),
        migrations.AlterField(
            model_name='post',
            name='temp_gpu_memory',
            field=models.CharField(max_length=50, default='204857600'),
        ),
    ]
