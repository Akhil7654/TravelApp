from django.shortcuts import render
from . models import meet
from . models import place
# Create your views here.

def home(request):
        obj1=meet.objects.all()
        obj2=place.objects.all()
        return render(request,"index.html",{"res":obj1,"results":obj2})

