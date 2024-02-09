from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm, IncomeTicketForm, ExpenseTicketForm
from .models import IncomeTicket, ExpenseTicket
from datetime import datetime


# Create your views here.


def expense_tracker(request):
    # Get all expense tickets and income tickets
    expense_tickets = ExpenseTicket.objects.all()
    income_tickets = IncomeTicket.objects.all()
    context = {'expense_tickets': expense_tickets, 'income_tickets': income_tickets}
    return render(request, 'ExpenseTracker/index.html', context)


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
        # See if the form is am Income Ticket
        if 'income_ticket' in request.POST:
            print('income_ticket')
            form = IncomeTicketForm(request.POST)
            if form.is_valid():
                source = form.cleaned_data['source']
                amount = form.cleaned_data['amount']
                user_id = request.user.id
                day = datetime.today().day
                month = datetime.today().month
                year = datetime.today().year
                income_ticket = IncomeTicket(amount=amount, source=source, day=day, month=month, year=year,
                                             user_id=user_id)
                # If the ticket saves I want an alert to tell the user that it saved correctly
                income_ticket.save()
        if 'expense_ticket' in request.POST:
            print('expense_ticket')
            form = ExpenseTicketForm(request.POST)
            if form.is_valid():
                item = form.cleaned_data['item']
                amount = form.cleaned_data['amount']
                user_id = request.user.id
                day = datetime.today().day
                month = datetime.today().month
                year = datetime.today().year
                expense_ticket = ExpenseTicket(amount=amount, source=item, day=day, month=month, year=year,
                                               user_id=user_id)
                # If the ticket saves I want an alert to tell the user that it saved correctly
                expense_ticket.save()

    income_form = IncomeTicketForm()
    expense_form = ExpenseTicketForm()

    return render(request, 'ExpenseTracker/new_item.html', {'income_form': income_form, 'expense_form': expense_form})
