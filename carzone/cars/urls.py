from django.urls import path

from carzone.cars.views import cars

urlpatterns = [
    path('', cars, name='cars'),

]