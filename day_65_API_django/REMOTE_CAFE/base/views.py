from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	
	return HttpResponse('hi there', content_type='text/plain')