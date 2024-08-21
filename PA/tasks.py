from celery import shared_task

@shared_task
def func():
    print("Task is running...")
    return func
