from django.shortcuts import render

from django. template import loader
from django.http import HttpResponse

from .models import Product

def homeView(request):
    
    template = loader.get_template('home.html')

    context = {

    }
    return HttpResponse(template.render(context, request))
