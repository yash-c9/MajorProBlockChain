from django.shortcuts import render
from django.template import loader

# Create your views here.

def home(request):

    return render(request, 'website/templates/index.html')