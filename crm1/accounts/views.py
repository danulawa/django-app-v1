from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def homePage(request):
    return render(request, 'accounts/dashboard.html')

def productsPage(request):
    return render(request, 'accounts/products.html')

def customerPage(request):
    return render(request, 'accounts/customer.html')
