from unicodedata import category
from django.shortcuts import render, redirect
from .forms import AddCafe
import csv
from csv import reader, writer



# Create your views here.
def home(request):
    return render(request, 'base/index.html')


def cafes(request):
    cafes = []
    with open('/home/huba/code/100_days_of_python/day_62_coffe_wifi_django/day_62_coffe_wifi_django/cafe-data.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
        for row in csv_reader:
            cafes.append(row)
            # row variable is a list that represents a row in csv
        
    categories = cafes[0]
    cafes = cafes[1:]
    # print(cafes[0:])
    # for cafe in cafes[0:]:
    #     print(cafe[0])

    context = {'cafes': cafes, 'categories': categories}
    return render(request, 'base/cafes.html', context)    


def add_new(request):
    form = AddCafe()
    context = {'form': form}
    form_data = AddCafe(request.POST or None)
    if form_data.is_valid():
        name = form_data.cleaned_data.get("name")
        location = form_data.cleaned_data.get("location")
        opening_hour = form_data.cleaned_data.get("opening_hour")
        closeing_hour = form_data.cleaned_data.get("closeing_hour")
        coffee = form_data.cleaned_data.get("coffee")
        wifi = form_data.cleaned_data.get("wifi")
        power = form_data.cleaned_data.get("power")
        
        List = [name, location, opening_hour, closeing_hour, coffee, wifi, power]

        with open('/home/huba/code/100_days_of_python/day_62_coffe_wifi_django/day_62_coffe_wifi_django/cafe-data.csv', 'a') as f_object: 
            writer_object = writer(f_object)
            writer_object.writerow(List)
            f_object.close()


    return render(request, 'base/add.html', context)    