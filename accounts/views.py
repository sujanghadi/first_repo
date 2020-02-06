from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import Orderform
from .forms import Customerform
# Create your views here.
def home(request):
    orders = Order.objects.all()
    customer = Customers.objects.all()

    Total_customers=customer.count()
    Total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()

    context={'orders':orders,'customers':customer,'Total_customers':Total_customers,'Total_orders':Total_orders,'delivered':delivered,'pending':pending}

    return render(request,'dashboard.html',context)
def product(request):
    product= Product.objects.all()

    return render(request,'products.html',{'products':product})
def customer(request,pk):
    customer=Customers.objects.get(id=pk)
    orders=customer.order_set.all()
    orders_count=orders.count()
    context={'customer':customer,'order':orders,'orders_count':orders_count}
    return render(request,'customer.html',context)

def createCustomer(request):
    form= Customerform
    if request.method=='POST':
        print(request.POST)
        form= Customerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context={'form':form}
    return render(request,"customerform.html",context)

def createOrder(request):
    form=Orderform
    if request.method=='POST':
        #print("Printing :",request.POST)
        form=Orderform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={'form':form}
    return render(request,"order_form.html",context)

def updateCustomer(request,pk):
    customers=Customers.objects.get(id=pk)
    form=Customerform(instance=customers)
    if request.method=='POST':
        print("Printing :",request.POST)
        form=Customerform(request.POST,instance=customers)
        if form.is_valid():
            form.save()
            return redirect("/")

    context={"form":form}
    return render(request,"customerform.html",context)

def UpdateOrder(request,pk):
    orders=Order.objects.get(id=pk)
    form=Orderform(instance=orders)
    if request.method=='POST':
        #print("Printing :",request.POST)
        form=Orderform(request.POST,instance=orders)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={'form':form}
    return render(request,"order_form.html",context)

def deleteOrder(request,pk):
    orders=Order.objects.get(id=pk)
    if request.method=='POST':
        orders.delete()
        return redirect("/")
    context={'item':orders}
    return render(request,"delete.html",context) 
