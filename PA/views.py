from django.shortcuts import render

from .tasks import print_nums

# Create your views here.

def index(request):
    # call celery task 
    print_nums.delay()
     
    return render(request,'index.html')