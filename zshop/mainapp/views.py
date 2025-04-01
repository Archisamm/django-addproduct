from django.shortcuts import render

from django. template import loader
from django.http import HttpResponse

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Product

def homeView(request):
    
    template = loader.get_template('home.html')

    context = {
        # context data to be pulled from the db
        'products' : Product.objects.all()
        # the above line of code is equivalent to SELECT * FROM product_table;
    }
    return HttpResponse(template.render(context, request))
class ProductDetails(DetailView):
    model = Product
    template_name = 'product_details.html'

def aboutView(request):
    template = loader.get_template('about.html')
    context = {}
    return HttpResponse(template.render(context, request))

def contactView(request):
    template = loader.get_template('contact.html')
    context = {}
    return HttpResponse(template.render(context, request))



#CRUD Opeartions




class AddProduct(CreateView):
    model = Product
    template_name = 'add_product.html'
    fields = '__all__'
    success_url = '/'


class EditProduct(UpdateView):
    model = Product
    context_object_name = 'product'
    template_name = 'edit_product.html'
    fields = ['img','price','stock']
    success_url = '/'


# D -Delete

class DelProduct(DeleteView):
    model = Product
    template_name = 'del_product.html'
    success_url = '/'
        
        
        
   



