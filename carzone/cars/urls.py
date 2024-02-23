from django.urls import path

from carzone.cars.views import cars, car_details

urlpatterns = [
    path('', cars, name='cars'),
    path('<int:id>/', car_details, name='car_details')

]