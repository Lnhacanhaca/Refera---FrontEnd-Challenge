from typing import ContextManager

import requests
from django.shortcuts import render
from .models import Order 
from django.contrib import messages


# Create your views here.
def home(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    clients = response.json()
    
    context = {
        'clients': clients
    }
    return render(request, 'index.htm', context=context)

def customer_form(request):
    return render(request, 'customer_form.htm')


def order(request):
    response = requests.get('https://api.jsonbin.io/b/61e1981aba87c130e3e84bb0')
    orders = response.json()
    dead = request.GET.get("deadline")
    objet = Order.objects.all()
    if dead is not None:
        objet = objet.filter(dead__id = dead)
        
    
    
    context = {
        'orders': orders,
        'objet': objet
    }
    return render(request, 'order.htm', context=context)

def order_form(request):
    return render(request, 'order_form.htm')




    