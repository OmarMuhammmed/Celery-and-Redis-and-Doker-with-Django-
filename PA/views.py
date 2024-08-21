from django.shortcuts import render

from .tasks import add

# Create your views here.

def index(request):
    # call celery task 
    
    result = add.delay(4, 6)
    print('celery is ruuuun')
    return render(request,'index.html',{'result':result})