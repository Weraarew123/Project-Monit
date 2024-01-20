from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "check/login.html")
# Create your views here.
