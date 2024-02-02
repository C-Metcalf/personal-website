from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm

# Create your views here.
# ToDo: Work on creating a login, sign-up, and logout functionality for this app.
#  it should use django built-in auth user to verify everything is secure.


def expense_tracker(request):
    return render(request, 'ExpenseTracker/index.html')


def signup(request):
    if request.method == 'POST':
        print(request.POST)
        form = SignupForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('ExpenseTracker:login')
        print('form was not valid')
    else:
        form = SignupForm()
    return render(request, 'ExpenseTracker/signup.html', {'form': form})


# login page
def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('ExpenseTracker:expense-tracker')
    else:
        form = LoginForm()
    return render(request, 'ExpenseTracker/login.html', {'form': form})


# logout page
def log_out(request):
    logout(request)
    return redirect('ExpenseTracker:login')
