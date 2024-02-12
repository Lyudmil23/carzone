from django.urls import path

from carzone.pages.views import home

urlpatterns = [
    path('', home, name='home'),
]