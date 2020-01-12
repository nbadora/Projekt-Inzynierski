from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Product
from .models import Service
from.models import New

# Create your views here.

class Index(View):
    template = 'news.html'

    def get(self, request):
        news = New.objects.all().order_by('-created_on')
        return render(request, 'news.html',{'News':news})

def prod(request):
    product = Product.objects.all()
    return render(request, 'products.html', {'Product': product})

def serv(request):
    service = Service.objects.all()
    return render(request, 'services.html', {'Service': service})

def abt(request):
    return render(request, 'about.html')

def cont(request):
    return render(request, 'contact.html')

def news(request):
    news = New.objects.all().order_by('-created_on')
    return render(request, 'news.html',{'News':news})

def prod_details(request,product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_details.html',{'Product':product})   

def serv_details(request,service_id):
    service = Service.objects.get(pk=service_id)
    return render(request, 'service_details.html',{'Service':service}) 