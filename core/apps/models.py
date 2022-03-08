from random import choices
from django.db import models

# Create your models here.

class Expenses(models.Model):
    DEBIT = 'Debit'
    CREDIT = 'Credit'
    n_choices = [
        (DEBIT, 'Debit'),
        (CREDIT, 'Credit')
    ]

    description = models.CharField(max_length=255)
    expense_type = models.CharField(max_length=100)
    amount = models.IntegerField()
    transaction = models.CharField(
        max_length=10,
        choices = n_choices,

    )

