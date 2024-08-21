from django.shortcuts import render
from .tasks import func
# Create your views here.

def index(request):
    # call celery task 
    func.delay()
    
    return render(request,'index.html',{})