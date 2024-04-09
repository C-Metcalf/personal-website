from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, ModelForm


class ContactForm(forms.Form):
    name = forms.CharField(widget=TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Enter your name...'}))

    email = forms.EmailField(widget=TextInput(attrs={'class': 'form-control',
                                                     'placeholder': 'Enter your email...'}))

    phone = forms.CharField(widget=TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Enter your phone number...'}))

    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                      'style': 'height: 10rem',
                                                      'placeholder': 'Enter your message...'}))
