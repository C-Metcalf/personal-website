from django.urls import path
from . import views

app_name = 'ExpenseTracker'
urlpatterns = [

    path('', views.expense_tracker, name='expense-tracker'),

    path('login/', views.log_in, name='login'),

    path('logout/', views.log_out, name='logout'),

    path('sign-up/', views.signup, name='sign-up'),
]
