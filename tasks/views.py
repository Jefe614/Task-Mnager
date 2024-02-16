from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

#logout
def logout(request):
    logout(request)
    return redirect('home')