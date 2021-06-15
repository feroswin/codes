from django.shortcuts import render
from django.http import HttpResponse
from .models import products

def index(request):
    products2 = products.objects.all()

    return render(request, "firstapp/index.html", {"products": products2, "title": "Список товаров"})

def about(request):
    return render(request, "firstapp/about.html")
