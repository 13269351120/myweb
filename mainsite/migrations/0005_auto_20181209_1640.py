# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20181208_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='DoPopulate',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='abs_pose_min_num_inliers',
            field=models.PositiveIntegerField(default=6),
        ),
        migrations.AddField(
            model_name='post',
            name='bin',
            field=models.CharField(default=b'/home/luban/jincheng_test/colmap/build/src/exe/', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='convert2grey_gpu',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='database_path',
            field=models.CharField(default=b'/nfs/project/daily_3drecon/20181122/3drecon/databases/samsung_starneto_1fps/database.db', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='faiss_gpu_device_index',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='faiss_knn_num',
            field=models.PositiveIntegerField(default=36),
        ),
        migrations.AddField(
            model_name='post',
            name='feature_extraction_device_index',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='geo_verify_type',
            field=models.CharField(default=b'neither', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='geomery_verify_ratio',
            field=models.FloatField(default=0.6),
        ),
        migrations.AddField(
            model_name='post',
            name='gps_filter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='index_path',
            field=models.CharField(default=b'/nfs/project/localization/faissindex/index_trained_SoftwareParkOne20180510_trained_NoPopulate.faissindex', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='index_type',
            field=models.CharField(default=b'faiss', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='max_focal_length_ratio',
            field=models.FloatField(default=1.2),
        ),
        migrations.AddField(
            model_name='post',
            name='max_image_size',
            field=models.PositiveIntegerField(default=2500),
        ),
        migrations.AddField(
            model_name='post',
            name='max_images_from_geomery_verify',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='post',
            name='max_localization_distance_against_gps',
            field=models.PositiveIntegerField(default=25),
        ),
        migrations.AddField(
            model_name='post',
            name='max_matching_distance',
            field=models.PositiveIntegerField(default=50),
        ),
        migrations.AddField(
            model_name='post',
            name='max_num_features',
            field=models.PositiveIntegerField(default=2500),
        ),
        migrations.AddField(
            model_name='post',
            name='max_num_images',
            field=models.PositiveIntegerField(default=20),
        ),
        migrations.AddField(
            model_name='post',
            name='min_co_visible_matches_num',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AddField(
            model_name='post',
            name='min_focal_length_ratio',
            field=models.FloatField(default=0.8),
        ),
        migrations.AddField(
            model_name='post',
            name='model_path',
            field=models.CharField(default=b'/nfs/project/daily_3drecon/20181122/3drecon/test_partial_ba/samsung_starneto_1fps/sparse', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='perf_test',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='perf_test_images',
            field=models.CharField(default=b'/nfs/project/localization/measure_set/software_park_two/20181129_samsung_test_1fps_00_01_filtered.txt', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='temp_gpu_memory',
            field=models.CharField(default=b'204857600', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='use_model_focal_length',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='use_opt_siftgpu',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='verify_score_threshold',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
