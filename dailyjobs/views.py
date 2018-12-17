from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template  

from django.http import HttpResponse
from .models import Dailyjobs  


def result(request , para):
	print("inside")
	htmlname = para + ".html"
	print (htmlname)
	template = get_template(''+htmlname)
	html = template.render()
	return HttpResponse(html)
	
	