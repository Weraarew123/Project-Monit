from django.http import HttpResponse
from django.shortcuts import render
from .tasks import http_response, add
import requests
from .models import Sites

def homePage(request):
    fullLink = {}
    links = Sites.objects.filter(user_owner=request.user)
    if links.exists():
        for link in links:
            r=requests.get(link.link)
            stat = r.status_code
            fullLink.update({link.link:stat})
            http_response.delay(link.link)
    context ={
        'links':fullLink,
    }
    return render(request, "check/home.html", context)

def tasker(request):
    return HttpResponse(add.delay(4,4))
