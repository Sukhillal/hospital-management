from django.shortcuts import render
from django.http import HttpResponse
from.models import Dep
from.models import Doctors
from.models import Booking
# from.django import from
from.forms import BookingForm
# Create your views here.
# def index(request):
#     return HttpResponse("blogs")

def index(request):
    return render(request,"index.html")

def register(request):
    return render(request,"register.html")

def about(request):
    persone={
        "name":"sukhil",
        "age":20
        
    }
    return render(request,"about.html",persone)


def number(request):
    num={
        "number":19
    }
    return render(request,"tags.html",num)

def num1(request):
    num2={
       "n": [1,2,3,4,5,6,7,8,9],
    }
    return render(request,"loop.html",num2)

def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
    
    
    form=BookingForm
    dict_form={
        "form":form
    }
    
    # book={
    #    " b":Booking.objects.all()
    # }
    return render(request,"booking.html",dict_form)

def department(request):
   dep= {
    "dep":Dep.objects.all()
   }
   return render(request,"dep.html",dep)

def doctors(request):
    doct={
        "d":Doctors.objects.all()
    }
    return render(request,"doc.html",doct)


