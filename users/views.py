from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.

def home(request):
    context = {}
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def profile(request):
    context = {}
    return render(request, 'profile.html', context)

