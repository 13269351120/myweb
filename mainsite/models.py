#-*- coding: utf-8 -*- 
from django.db import models

# Create your models here.


from django.utils import timezone

class Post(models.Model):
	
	testname = models.CharField(max_length=50)
	
	parameters = models.CharField(max_length=50)
	
	bin = models.CharField(max_length = 200 , default = "/home/luban/jincheng_test/colmap/build/src/exe/")
	geomery_verify_ratio = models.FloatField(default=0.6)
	max_images_from_geomery_verify = models.PositiveIntegerField(default=10)
	camera_focal_length_type = models.IntegerField(default=2)
	provided_focal_length = models.FloatField(default = 1850.0)
	estimate_focal_length = models.FloatField(default = 0 ) 
	feature_extraction_device_index = models.IntegerField(default = 0)
	perf_test = models.IntegerField(default=1)
	index_type  = models.CharField(max_length = 20 , default = "faiss")
	max_num_images = models.PositiveIntegerField(default=20)
	abs_pose_min_num_inliers = models.PositiveIntegerField(default=6)
	min_focal_length_ratio = models.FloatField(default=0.8)
	max_focal_length_ratio = models.FloatField(default=1.2)
	max_matching_distance = models.PositiveIntegerField(default=50)
	max_localization_distance_against_gps = models.PositiveIntegerField(default=25)
	max_image_size = models.PositiveIntegerField(default=2500)
	max_num_features = models.PositiveIntegerField(default=2500)
	gps_filter = models.IntegerField(default=0)
	faiss_knn_num = models.PositiveIntegerField(default=36)
	min_co_visible_matches_num = models.PositiveIntegerField(default=3)
	geo_verify_type = models.CharField(max_length = 50 , default = "neither")
	verify_score_threshold = models.PositiveIntegerField(default = 5)
	temp_gpu_memory = models.CharField(max_length = 50 , default= "204857600")
	use_opt_siftgpu = models.IntegerField(default = 0)
	convert2grey_gpu = models.IntegerField(default = 0 )
	DoPopulate = models.IntegerField(default = 1 )
	faiss_gpu_device_index = models.IntegerField(default = 0 )
	index_path = models.CharField(max_length = 500 , default = "/nfs/project/localization/faissindex/index_trained_SoftwareParkOne20180510_trained_NoPopulate.faissindex")
	model_path =  models.CharField(max_length = 500 , default = "/nfs/project/daily_3drecon/20181122/3drecon/test_partial_ba/samsung_starneto_1fps/sparse")
	perf_test_images = models.CharField(max_length = 500 , default = "/nfs/project/localization/measure_set/software_park_two/20181129_samsung_test_1fps_00_01_filtered.txt")
	database_path = models.CharField(max_length = 500 , default = "/nfs/project/daily_3drecon/20181122/3drecon/databases/samsung_starneto_1fps/database.db")
	
	pub_date = models.DateTimeField(default=timezone.now , editable = False)
	user = models.CharField(max_length = 20)
	state = models.IntegerField(default=0 , editable = False )  
	
	mean_error = models.FloatField(default = -1.0,editable = False)  
	medium_error = models.FloatField(default = -1.0,editable = False)
	time_cost = models.FloatField(default = -1.0 ,editable = False)
	
	class Meta:
		ordering = ('-pub_date',)
		
	
	def __unicode__(self):
		return self.parameters  
		
