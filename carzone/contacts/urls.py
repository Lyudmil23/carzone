from django.urls import path

from carzone.contacts.views import inquiry

urlpatterns = [
    path('inquiry', inquiry, name='inquiry'),

]