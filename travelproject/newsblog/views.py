from django.shortcuts import render

# Create your views here.
from newsblog.models import blog


def news(request):
    obj4=blog.objects.all()
#     # return render(request,'index.html',{'newses':obj4})
