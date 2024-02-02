from django.http import HttpResponse
from django.shortcuts import render
from .tasks import add

def homePage(request):
    return render(request, "check/home.html")

def tasker(request):
    return HttpResponse(add.delay(4,4))
