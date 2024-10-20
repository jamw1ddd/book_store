from django.shortcuts import render
from .models import Product

def home_view(request):
    products = Product.objects.all().order_by('-id')[:4]
    return render(request,'index.html',{'products': products})

def products_view(request):
    product = Product.objects.all().order_by('-id')[:4]
    return render(request,'subpage.html',{'product': product})