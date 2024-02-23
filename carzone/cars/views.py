from django.http import HttpResponse
from django.shortcuts import render


def cars(request):
    return render(request, 'cars/cars.html')


def car_details(request, id):
    return render(request, 'cars/car-details.html')
