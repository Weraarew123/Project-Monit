from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name="check/login.html"), name='login'),
    path('home/', views.homePage, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/edit/<int:pk>', views.edit_link, name='edit_link'),
    path('logout/delete/<int:pk>', views.delete_link, name='delete_link'),
]
