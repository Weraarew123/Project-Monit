from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name="check/login.html")),
    path('home/', views.homePage, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('tasky/', views.schedulePage)
]
