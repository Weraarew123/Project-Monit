from celery import shared_task
from celery.utils.log import get_task_logger
from django.shortcuts import get_object_or_404, redirect
import requests
from .models import Sites

logger = get_task_logger(__name__)

@shared_task
def http_response(link):
    r = requests.get(link)
    stat = r.status_code
    obj = get_object_or_404(Sites, link=link)
    obj.status = stat
    obj.save()
    return redirect('home')

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)