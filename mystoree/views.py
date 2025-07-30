from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm

# Create your views here.
def home(request):
    return render(request ,'mystoree/home.html')

def profile(request):
    return render(request,'mystoree/profile.html')

def imported(request):
    return render(request,'mystoree/imported.html')


def business(request):
    return render(request,'mystoree/business.html')



def customer(request):
    items = Customer.objects.all()
    return render(request,'mystoree/customer.html',{'items':items})

def addcustomer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('mystoree:customer')
    return render(request ,'mystoree/addcustomer.html',{'form':form})

def details(request,id):
    cus = Customer.objects.get(pk=id)
    return render(request ,'mystoree/details.html',{'cus': cus})

def delete(request,id):
    cus = Customer.objects.get(pk=id)
    if request.method == 'POST':
        cus.delete()
        return redirect('mystoree:customer')
    return render(request,'mystoree/delete.html',{'cus':cus})


def update(request,id):
    cus = Customer.objects.get(pk=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST , instance=cus)
        if form.is_valid():
            form.save()
            return redirect('mystoree:customer')
    else:
        form = CustomerForm(instance=cus)
    return render(request,'mystoree/update.html',{'form':form})



