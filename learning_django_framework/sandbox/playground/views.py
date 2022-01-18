from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    x = 2
    y = 3
    return render(request, 'hello.html', {'name': 'Huba'})