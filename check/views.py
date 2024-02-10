from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from check.forms import EditLinkForm
from .tasks import http_response, add
import requests
from .models import Sites
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
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
        'full_link':fullLink,
        'links':links,
    }
    return render(request, "check/home.html", context)

def edit_link(request, pk):
    site = get_object_or_404(Sites, pk=pk)
    if request.method=='POST':
        form = EditLinkForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = EditLinkForm(instance=site)
    context={
        'form':form,
        'site':site,
    }
    return render(request, 'check/edit_link.html', context)

def delete_link(request, pk):
    site = get_object_or_404(Sites, pk=pk)
    site.delete()
    return redirect('home')
