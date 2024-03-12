from django.shortcuts import render
from . models import place
from . models import person
def demo(request):
    oj=place.objects.all()
    oj2=person.objects.all()
    return render(request, "index.html", {'result': oj,'result1':oj2})
# def demo1(request):
#     oj2=person.objects.all()
#     return render(request,"index.html",{'result1':oj2})
# Create your views here.

