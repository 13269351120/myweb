from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from .models import Post  


def ChooseParameters(request):
	posts = Post.objects.all() 
	post_lists = list() 
	for count , post in enumerate(posts,1):
		post_lists.append("No.{}:".format(str(count)) + str(post) + "<br>") 
	return HttpResponse(post_lists)
	
	