# Generated by Django 5.0.1 on 2024-02-09 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExpenseTracker', '0008_remove_expenseticket_day_remove_expenseticket_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenseticket',
            name='day',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='expenseticket',
            name='month',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='expenseticket',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='incometicket',
            name='day',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='incometicket',
            name='month',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='incometicket',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]
