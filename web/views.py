from json import JSONEncoder
from django.shortcuts import render
from django.http import JsonResponse
from web.models import User, Token, Expense, Income
from datetime import datetime

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def submit_expense(request):
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    Expense.objects.create(user=this_user, amount=request.POST['amount'],
                           text=request.POST['text'], date=datetime.now())

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)


@csrf_exempt
def submit_income(request):
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    Income.objects.create(user=this_user, amount=request.POST['amount'],
                           text=request.POST['text'], date=datetime.now())

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)