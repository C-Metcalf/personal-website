from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class ExpenseTicket(models.Model):
    item = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class IncomeTicket(models.Model):
    source = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
