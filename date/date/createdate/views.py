from django.shortcuts import render

# Create your views here.
import datetime


def create(request):

    today = {'name': 'Ramesh', 't': datetime.datetime.now()}
    return render(request, 'home.html', context=today)

