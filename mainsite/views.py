# -*- coding: utf-8 -*- 
from django.shortcuts import render
import os
import datetime
# Create your views here.


from django.http import HttpResponse
from .models import Post  
from django.shortcuts import redirect  
  
from django.template.loader import get_template  

from .form import LogForm

def ChooseParameters(request):
	if(request.method == 'POST'):
		print("post post")
	if(request.method == 'GET'):
		print("get get")
	template = get_template('post.html')
	print("template ok")
	html = template.render()
	print("html ok")
	return HttpResponse(html)
	
#	posts = Post.objects.all() 
#	post_lists = list() 
#	for count , post in enumerate(posts,1):
#		post_lists.append("No.{}:".format(str(count)) + str(post)  +"<br>") 
#	return HttpResponse(post_lists)
	
	
#
#def SubmitParameters(request , slug ):
#	posts = Post.objects.get(slug=slug) 
#	if(post != None) :
#		html = template.render(local())  
#		return HttpResponse(html)
#		
#	except:
#		return redirect('/')
	
def QueryList(request):
	
	
	
	return HttpResponse 
	
def postlist(request):
	message = ""
	if(request.method == 'POST'):
		print("post post")
		form = LogForm(request.POST)
		
		if(form.is_valid()):
			print("form is valid")
			bin = form.cleaned_data['bin']
			Geomery_verify_ratio = form.cleaned_data['Geomery_verify_ratio']
			Max_images_from_geomery_verify = form.cleaned_data['Max_images_from_geomery_verify'] 
			#Use_model_focal_length = form.cleaned_data['Use_model_focal_length'] 
			Camera_focal_length_type = form.cleaned_data['Camera_focal_length_type']
			Provided_focal_length = form.cleaned_data['Provided_focal_length']
			Estimate_focal_length = form.cleaned_data['Estimate_focal_length']
			Feature_extraction_device_index = form.cleaned_data['Feature_extraction_device_index'] 
			Perf_test = form.cleaned_data['Perf_test'] 
			Index_type = form.cleaned_data['Index_type'] 
			Max_num_images = form.cleaned_data['Max_num_images'] 
			Abs_pose_min_num_inliers = form.cleaned_data['Abs_pose_min_num_inliers'] 
			Min_focal_length_ratio = form.cleaned_data['Min_focal_length_ratio'] 
			Max_focal_length_ratio = form.cleaned_data['Max_focal_length_ratio'] 
			Max_matching_distance = form.cleaned_data['Max_matching_distance'] 
			Max_localization_distance_against_gps = form.cleaned_data['Max_localization_distance_against_gps'] 
			Max_image_size = form.cleaned_data['Max_image_size'] 
			Max_num_features = form.cleaned_data['Max_num_features'] 
			Gps_filter = form.cleaned_data['Gps_filter'] 
			Faiss_knn_num = form.cleaned_data['Faiss_knn_num'] 
			Min_co_visible_matches_num = form.cleaned_data['Min_co_visible_matches_num'] 
			Geo_verify_type = form.cleaned_data['Geo_verify_type'] 
			Verify_score_threshold = form.cleaned_data['Verify_score_threshold'] 
			Temp_gpu_memory = form.cleaned_data['Temp_gpu_memory'] 
			Use_opt_siftgpu = form.cleaned_data['Use_opt_siftgpu'] 
			Convert2grey_gpu = form.cleaned_data['Convert2grey_gpu'] 
			DoPopulate = form.cleaned_data['DoPopulate'] 
			Faiss_gpu_device_index = form.cleaned_data['Faiss_gpu_device_index'] 
			Index_path = form.cleaned_data['Index_path'] 
			Model_path = form.cleaned_data['Model_path'] 
			Perf_test_images = form.cleaned_data['Perf_test_images'] 
			Database_path = form.cleaned_data['Database_path'] 
			User = form.cleaned_data['User'] 
			Testname = form.cleaned_data['Testname'] 
			
			
			print("------------------------------------------------",)
			print("bin:" ,bin)
			print("Geomery_verify_ratio",Geomery_verify_ratio)
			print("Max_images_from_geomery_verify",Max_images_from_geomery_verify)
			#print("Use_model_focal_length",Use_model_focal_length)
			print("Feature_extraction_device_index",Feature_extraction_device_index)
			print("Perf_test",Perf_test)
			print("Index_type",Index_type)
			print("Max_num_images",Max_num_images)
			print("Abs_pose_min_num_inliers",Abs_pose_min_num_inliers)
			print("Min_focal_length_ratio",Min_focal_length_ratio)
			print("Max_focal_length_ratio",Max_focal_length_ratio)
			print("Max_matching_distance",Max_matching_distance)
			print("Max_localization_distance_against_gps",Max_localization_distance_against_gps)
			print("Max_image_size",Max_image_size)
			print("Max_num_features",Max_num_features)
			print("Gps_filter",Gps_filter)
			print("Faiss_knn_num",Faiss_knn_num)
			print("Min_co_visible_matches_num",Min_co_visible_matches_num)
			print("Geo_verify_type",Geo_verify_type)
			print("Verify_score_threshold",Verify_score_threshold)
			print("Temp_gpu_memory",Temp_gpu_memory)
			print("Use_opt_siftgpu",Use_opt_siftgpu)
			print("Convert2grey_gpu",Convert2grey_gpu)
			print("DoPopulate",DoPopulate)
			print("Faiss_gpu_device_index",Faiss_gpu_device_index)
			print("Index_path",Index_path)
			print("Model_path",Model_path)
			print("Perf_test_images",Perf_test_images)
			print("Database_path",Database_path)
			print("User",User)
			print("Testname",Testname)
			print("------------------------------------------------",)
			
			now = datetime.datetime.now().strftime('%Y%m%d_%H_%M_%S')
			dirname = "/nfs/project/localization/monitor/dailyjobs/" + str(User) + "/"
			#dirname = "/home/sth/nfs/project/localization/monitor/dailyjobs/" + str(User) + "/"
			print(dirname)
			if(os.path.exists(dirname) == False):
				os.makedirs(dirname)
			else :
				print("目录已经存在")
			
			filename = dirname + Testname + "_" + now +".sh"
			print(filename)

			file = open(filename,"w")

			print("创建文件.sh")
			print("bin:" ,bin)
			content = \
			"PROJECT_PATH=$1 \n" \
			'bin='+ '"' + str(bin)+ '"' "; \n"\
			"$bin/localization_server \ \n \
			--SiftMatching.geomery_verify_ratio " + str(Geomery_verify_ratio) + " \  \n \
			--SiftMatching.max_images_from_geomery_verify "+ str(Max_images_from_geomery_verify)+ " \ \n \
			--Localization.camera_focal_length_type " + str(Camera_focal_length_type) + "\ \n \
			--Localization.provided_focal_length " + str(Provided_focal_length) + "\ \n \
			--Localization.estimate_focal_length " + str(Estimate_focal_length) + "\ \n \
			--Localization.feature_extraction_device_index "+ str(Feature_extraction_device_index) +"\n \
			--Localization.perf_test "+ str(Perf_test) +" \ \n \
			--Localization.index_type "+ str(Index_type) +" \ \n \
			--Localization.max_num_images "+ str(Max_num_images) +" \ \n \
			--Localization.abs_pose_min_num_inliers "+ str(Abs_pose_min_num_inliers) +" \ \n \
			--Localization.min_focal_length_ratio "+ str(Min_focal_length_ratio) +" \ \n \
			--Localization.max_focal_length_ratio "+ str(Max_focal_length_ratio) +" \ \n \
			--Localization.max_matching_distance "+ str(Max_matching_distance) +" \ \n \
			--Localization.max_localization_distance_against_gps "+ str(Max_localization_distance_against_gps) +" \ \n \
			--Localization.max_image_size "+ str(Max_image_size) +" \ \n \
			--Localization.max_num_features "+ str(Max_num_features) +" \ \n \
			--Localization.gps_filter "+ str(Gps_filter) +" \ \n \
			--LocalizationFaiss.faiss_knn_num "+ str(Faiss_knn_num) +" \ \n \
			--LocalizationFaiss.min_co_visible_matches_num "+ str(Min_co_visible_matches_num) +" \ \n \
			--LocalizationFaiss.geo_verify_type "+ str(Geo_verify_type) +" \ \n \
			--LocalizationFaiss.verify_score_threshold "+ str(Verify_score_threshold) +" \ \n \
			--LocalizationFaiss.temp_gpu_memory "+ str(Temp_gpu_memory) +" \ \n \
			--Localization.use_opt_siftgpu "+ str(Use_opt_siftgpu) +" \ \n \
			--Localization.convert2grey_gpu "+ str(Convert2grey_gpu) +" \ \n \
			--FaissIndexOptions.DoPopulate "+ str(DoPopulate) +" \ \n \
			--FaissIndexOptions.faiss_gpu_device_index "+ str(Faiss_gpu_device_index) +" \ \n \
			--FaissIndexOptions.index_path "+ str(Index_path) +" \ \n \
			--Localization.model_path "+ str(Model_path) +" \ \n \
			--Localization.perf_test_images "+ str(Perf_test_images) +" \ \n \
			--Localization.database_path "+ str(Database_path)  +"  \n"


			file.write(content)


			file.close()
			
     
      
			
		else :
			print("form is not valid")
	#		message =
	if(request.method == 'GET'):
		print("get get")
	posts = Post.objects.all() 
	post_lists = list() 
	for count , post in enumerate(posts,1):
		post_lists.append("No.{}:".format(str(count)) + str(post)  +"<br>") 
	return HttpResponse(post_lists)
	
