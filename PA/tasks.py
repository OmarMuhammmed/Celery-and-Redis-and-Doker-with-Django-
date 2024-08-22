import time
from celery import shared_task

@shared_task
def print_nums():
   for x in range(10):
        print(x)
        time.sleep(.5)