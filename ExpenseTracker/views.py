from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm, IncomeTicketForm
from .models import IncomeTicket
from datetime import datetime

# Create your views here.


def expense_tracker(request):
    return render(request, 'ExpenseTracker/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ExpenseTracker:login')
        else:
            print(request.POST)
            print(form.errors)
    else:
        form = SignupForm()
    return render(request, 'ExpenseTracker/signup.html', {'form': form})


# login page
def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('ExpenseTracker:expense-tracker')
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'ExpenseTracker/login.html', {'form': form})


# logout page
def log_out(request):
    logout(request)
    return redirect('ExpenseTracker:login')


def new_item(request):
    if request.method == 'POST':
        form = IncomeTicketForm(request.POST)
        if form.is_valid():
            source = form.cleaned_data['source']
            amount = form.cleaned_data['amount']
            user_id = request.user.id
            date = datetime.date(datetime.now())
            income_ticket = IncomeTicket(amount=amount, source=source, date=date ,user_id=user_id)
            income_ticket.save()
    else:
        form = IncomeTicketForm()

    return render(request, 'ExpenseTracker/new_item.html', {'form': form})


