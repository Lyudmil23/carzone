from django.urls import path

from carzone.cars.views import cars, car_details, search

urlpatterns = [
    path('', cars, name='cars'),
    path('<int:id>/', car_details, name='car_details'),
    path('search/', search, name='search'),

]