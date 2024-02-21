from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from .forms import CustomAuthenticationForm, RegistrationForm


# Create your views here.
def homepage(request):
    return render(request, 'home.html')

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
            form.save()
            # Redirect to a success page or login page
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html')
#logout
def logout(request):
    logout(request)
    return redirect('home')