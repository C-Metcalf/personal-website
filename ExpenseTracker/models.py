from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class ExpenseTicket(models.Model):
    item = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    day = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # I want this to be a dropdown where the user selects the category instead of typing one in
    # This would then be a table with in the db where the users could add categories but not remove them.
    # category = models.CharField(max_length=50)

    def date(self):
        return f"{self.month}-{self.day}-{self.year}"


class IncomeTicket(models.Model):
    source = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    day = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def date(self):
        return f"{self.month}-{self.day}-{self.year}"
