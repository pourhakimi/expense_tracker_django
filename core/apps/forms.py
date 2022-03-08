from django import forms
from .models import Expenses

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ('description', 'expense_type', 'amount', 'transaction')
        labels = {
            'expense_type': 'Expense Type'
        }
    
    def __init__(self, *args,**kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['transaction'].empty_label = "Select"