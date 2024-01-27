from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def loginPage(request):
    if request.method =="POST":
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        
        user = authenticate(request, username=username, password = passwd)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, "check/login.html")

def homePage(request):
    return render(request, "check/home.html")
# Create your views here.
