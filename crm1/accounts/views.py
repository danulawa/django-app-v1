from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def homePage(request):
    return HttpResponse('Home Page')

def productsPage(request):
    return HttpResponse('Product Page')

def customerPage(request):
    return HttpResponse('Customer Profile')
