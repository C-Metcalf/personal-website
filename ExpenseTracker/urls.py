from django.urls import path
from . import views

app_name = 'ExpenseTracker'
urlpatterns = [

    path('', views.expense_tracker, name='portfolio'),

    path('login/', views.login, name='login'),

    path('logout/', views.logout, name='logout'),

    path('sign-up/', views.signup, name='sign-up'),
]
