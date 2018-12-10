from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from .models import Post  
from django.shortcuts import redirect  
from datetime import datetime  
from django.template.loader import get_template  

from .form import LogForm

def ChooseParameters(request):
	if(request.method == 'POST'):
		print("post post")
	if(request.method == 'GET'):
		print("get get")
	template = get_template('post.html')
	html = template.render()
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
	
	posts = Post.objects.all() 
	
	return HttpResponse 
	
def postlist(request):
	if(request.method == 'POST'):
		print("post post")
		form = LogForm(request.POST)
		
		if(form.is_valid()):
			print("form is valid")
			bin = form.cleaned_data['bin']
			Geomery_verify_ratio = form.cleaned_data['Geomery_verify_ratio']
			print("bin:" ,bin)
			print("Geomery_verify_ratio",Geomery_verify_ratio)
		else :
			print("form is not valid")
			
	if(request.method == 'GET'):
		print("get get")
	posts = Post.objects.all() 
	post_lists = list() 
	for count , post in enumerate(posts,1):
		post_lists.append("No.{}:".format(str(count)) + str(post)  +"<br>") 
	return HttpResponse(post_lists)
	