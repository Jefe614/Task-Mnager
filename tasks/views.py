from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from .forms import CustomAuthenticationForm, RegistrationForm
from django.contrib.auth.models import User
from .models import *
from rest_framework import generics
from .serializers import TaskSerializer


# Create your views here.
def homepage(request):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'home.html', {'tasks': tasks,'categories': categories,'products':products})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error_message = "Invalid username or password. Please try again."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = CustomAuthenticationForm()
            
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, email=email, password=password)
            # Redirect to a success page or login page
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html')
#logout
def logout(request):
    logout(request)
    return redirect('home')


def product_list(request):
    queryset = Product.objects.all()
    category = request.GET.get('category')
    if category:
        queryset = queryset.filter(category=category)
    return render(request, 'product_list.html', {'products': queryset})

def product_list(request):
    queryset = Product.objects.all()
    sort_by = request.GET.get('sort_by')
    if sort_by == 'name':
        queryset = queryset.order_by('name')
    elif sort_by == 'price':
        queryset = queryset.order_by('price')
    return render(request, 'product_list.html', {'products': queryset})


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer