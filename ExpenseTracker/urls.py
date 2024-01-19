from django.urls import path

from . import views

app_name = 'ExpenseTracker'
urlpatterns = [

    path('', views.expense_tracker, name='portfolio'),

]
