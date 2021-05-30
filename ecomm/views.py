from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from ecomm.models import Product
from ecomm.forms import CartForm,CreateUserForm
from ecomm.myapp import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate






# Create your views here.
def index(request):
    p=Product.objects.all()
    
    return render(request, 'index1.html',{'p':p})

def detail(request,product_id,slug):
    d = Product.objects.get(id=product_id)

    if request.method == 'POST':
        f = CartForm(request,request.POST)
        if  f.is_valid():
            request.form_data = f.cleaned_data
            add_to_cart(request)
            return redirect('ecomm:cart')
    f = CartForm(request, initial= {'product_id':product_id})
    return render(request,'detail.html',{'d':d,'f':f})

def cart_view(request):
    if request.method == "POST" and request.POST.get('delete') == "Delete":
        item_id = request.POST.get('item_id')
        cd=Cart.objects.filter(id=item_id)
        cd.delete()
    c = get_cart(request)
    t = total(request)
    co = item_count(request)
    return render(request,'cart.html',{'c':c,'t':t,'co':co})
    
def register(request):
    
    f=CreateUserForm
    if request.method=='POST':
        f=CreateUserForm(request.POST)
        if f.is_valid():
            f.save()
            print("user created")
            return redirect('ecomm:intermediate')
        else:
            return redirect('ecomm:register')
    return render(request, "register.html",{'f':f})

def loginpage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            print('logged in')
        return redirect('ecomm:index')

    return render(request, "login.html")
def logoutpage(request):
    logout(request)
    return redirect('ecomm:index')

def intermediate(request):
    return render(request, "intermediate.html")


