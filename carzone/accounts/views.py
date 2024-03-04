from django.contrib import messages
from django.shortcuts import render, redirect


def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        messages.error(request, 'This is error message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')




def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    return redirect('home')