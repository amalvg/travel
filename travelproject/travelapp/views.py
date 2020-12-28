from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render


from .models import place, special, news


def fun(request):
    obj=place.objects.all()
    obj1=special.objects.all()
    obj2=news.objects.all()
    return render(request,'index.html',{"results":obj,"packs":obj1,'newses':obj2})


def addition(request):
    # num1=int(request.GET['num1'])
    num1 = int(request.POST['num1'])
    # num2=int(request.GET['num2'])
    num2 = int(request.POST['num2'])
    num3=num1+num2
    return render(request,'index.html',{'add':num3})