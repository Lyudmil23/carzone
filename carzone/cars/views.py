from django.http import HttpResponse
from django.shortcuts import render


def cars(request):
    return render(request, 'cars/cars.html')
