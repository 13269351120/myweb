from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from .models import Dailyjobs  


def result(request):
	results = Dailyjobs.objects.all() 
	results_lists = list() 
	for count , res in enumerate(results,1):
		
		if res.state == 0 :
			results_lists.append("No.{}:".format(str(count)) + str(res) + "state is {}:".format(res.state) + "mean_error :{}".format(res.mean_error) + \
			"medium_error :{}".format(res.medium_error) + "time_cost :{}".format(res.time_cost) + "<br>") 
	return HttpResponse(results_lists)
	
	