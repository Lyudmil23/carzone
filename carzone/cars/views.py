from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from carzone.cars.models import Car


def cars(request):
    return render(request, 'cars/cars.html')


def car_details(request, id):
    single_car = get_object_or_404(Car, pk=id)
    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car-details.html', data)
