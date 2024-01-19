from django.urls import path

from . import views

app_name = 'Portfolio'
urlpatterns = [

    path('', views.portfolio, name='portfolio'),

    path('projects/', views.projects, name='projects'),

    path('resume/', views.resume, name='resume'),

    path('contact/', views.contact, name='contact'),

]
