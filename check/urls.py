from django.urls import path

from . import views

app_name = "check"
urlpatterns = [
    path('', views.home, name='home')
]
