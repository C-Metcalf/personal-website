from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, ModelForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 250px;',
                'placeholder': 'JohnDoe'
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 250px;',
                'placeholder': 'JohnDoe'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 250px;',
                'placeholder': 'JohnDoe'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 250px;',
                'placeholder': 'JDoe@gmail.com'
            }),
            'password1': PasswordInput(attrs={
                'class': 'form-control',
                'style': 'width: 250px;',
                'placeholder': 'Password'

            }),
            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'style': 'width: 250px;',
                'placeholder': 'Confirm Password'
            })
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'style': 'width: 250px;',
                                                             'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                             'style': 'width: 250px;',
                                                             'placeholder': 'Password'}))


class IncomeTicketForm(forms.Form):
    source = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'style': 'width: 275px; margin: auto',
                                                             'placeholder': 'Where did you get the money from'}))
    amount = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                                             'style': 'width: 275px; margin: auto',
                                                             'placeholder': 'How much money did you get'}))

class ExpenseTicketForm(forms.Form):
    item = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'style': 'width: 275px; margin: auto',
                                                         'placeholder': 'What did you spend money on?'}))

    amount = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                'style': 'width: 275px; margin: auto',
                                                                'placeholder': 'How much money did you spend?'}))


