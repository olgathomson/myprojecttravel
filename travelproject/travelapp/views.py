from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    name="india"
    return render(request,"index1.html",{'obj':name})
def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res=x+y
    return render(request,"result.html",{'result':res})
# def about(request):
#     return render(request,"about1.html")
# def contact(request):
#     return HttpResponse("I am contact")