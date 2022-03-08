from django.shortcuts import redirect, render
from .forms import ExpenseForm
from .models import Expenses
from django.db.models import Sum

# Create your views here.

def expense_list(request):
    context = {'expense_list': Expenses.objects.all()}
    return render(request, "apps/expense_list.html", context)

def expense_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ExpenseForm()
        else:
            expense = Expenses.objects.get(pk = id)
            form = ExpenseForm(instance = expense)
        return render(request, "apps/expense_form.html",{'form': form})
    else:
        if id == 0:
            form = ExpenseForm(request.POST)
        else:
            expense = Expenses.objects.get(pk = id)
            form = ExpenseForm(request.POST, instance = expense)
        if form.is_valid():
            form.save()
        return redirect('/expense/list')

def expense_delete(request, id):
    expense = Expenses.objects.get(pk=id)
    expense.delete()
    return redirect('/expense/list')

def expense_show(request):
    return redirect('/expense/')

# def sum(request, amount):
#     # https://www.youtube.com/watch?v=oHJF9mfswzo

def add_expense(request):
    data = Expenses.objects.all().aggregate(data = Sum('amount'))
    print(data)
    return render(request, 'apps/expense_list.html', {"data": data})