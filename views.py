from django.shortcuts import render
from django.http import HttpResponse

def home(request):
 return render(request,'home.html')

def mobile(request):
 return render(request,'mobile.html')

def profile(request):
 return render(request,'profile.html')

def orders(request):
 return render(request, 'orders.html')

def change_password(request):
 return render(request, 'changepassword.html')

def add_to_cart(request):
 return render(request, 'addtocart.html')

def login(request):
 return render(request, 'login.html')

def customerregistration(request):
 return render(request, 'customerregistration.html')

def product_detail(request):
 return render(request, 'productdetail.html')


# Create your views here.
