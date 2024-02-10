from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
    
class Sites(models.Model):
    link = models.CharField(max_length=200)
    user_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, editable=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Sites'
    @admin.display(
        boolean= False,
        ordering='userId',
        description='strony internetowe',
    )
    def __str__(self):
        return self.link
    
# Create your models here.
