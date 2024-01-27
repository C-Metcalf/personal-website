from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm

# Create your views here.
# ToDo: Work on creating a login, sign-up, and logout functionality for this app.
#  it should use django built-in auth user to verify everything is secure.


def expense_tracker(request):
    return render(request, 'ExpenseTracker/base.html')


def signup(request):
    if request.method == 'POST':
        print(request.POST['password1'])
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        print('form was not valid')
        #print(form)
    else:
        form = UserCreationForm()
    return render(request, 'ExpenseTracker/signup.html', {'form': form})


# login page
def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print('valid form')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'ExpenseTracker/login.html', {'form': form})


# logout page
def log_out(request):
    logout(request)
    return redirect('login')
