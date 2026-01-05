from django.shortcuts import render
from .models import Bangjobs,Punejobs,Biharjobs


# Create your views here.
def indexViews(request):
    return render(request,'testapp/index.html')

def BangViews(request):
    data=Bangjobs.objects.all()
    return render(request,'testapp/bang.html',{'data':data})

def PuneViews(request):
    data=Punejobs.objects.all()
    return render(request,'testapp/pune.html',{'data':data})

def BiharViews(request):
    data=Biharjobs.objects.all()
    return render(request,'testapp/bihar.html',{'data':data})
    
