from django.shortcuts import render
from .models import Schedule, Date
# Create your views here.

def collect(request):
    context = {'schedule' : Schedule}
    return render(request, 'list.html', context)

def arrange(request):
    context = {'date': Date}
    return render(request, 'order.html', context)