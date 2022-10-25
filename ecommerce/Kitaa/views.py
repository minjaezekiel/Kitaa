from django.shortcuts import render
from django.http import HttpResponse
from . models import Items

# Create your views here.
def home(request):
    item = Items.objects.all()
    context = {'item':item }
    return render (request, 'Kitaa/home.html', context)
    
    
