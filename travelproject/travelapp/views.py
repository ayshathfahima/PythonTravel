from django.http import HttpResponse
from django.shortcuts import render
from . models import Place, Team


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    item=Team.objects.all()

    return render (request,"index.html", {'result':obj , 'next':item})
#
# def addition(request):
#     x= int(request.GET['num1'])
#     y= int(request.GET['num2'])
#     res=x+y
#     return render (request, "result.html",{'result':res})