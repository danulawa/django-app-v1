from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage),
    path('products/', views.productsPage),
    path('customer/', views.customerPage),
]