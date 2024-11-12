from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, ModelForm
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


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

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
