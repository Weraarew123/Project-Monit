from django.http import HttpResponse
from django.shortcuts import redirect, render
from .tasks import http_response, add
import requests
from .models import Sites

def homePage(request):
    if request.method=='POST':
        site = Sites()
        site.user_owner = request.user
        site.link = request.POST['strona']
        site.save()
        return redirect('home')
    fullLink = {}
    links = Sites.objects.filter(user_owner=request.user)
    if links.exists():
        for link in links:
            try:
                r=requests.get(link.link)
                stat = r.status_code  
                http_response.delay(link.link)     
            except:
                stat = 'NOT WORKING'
            fullLink.update({link.link:stat})
    context ={
        'links':fullLink,
    }
    return render(request, "check/home.html", context)
