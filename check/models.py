from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
    
class Sites(models.Model):
    link = models.URLField(max_length=200)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    @admin.display(
        boolean= True,
        ordering='userId',
        description='strony internetowe',
    )
    def __str__(self):
        return self.link
    
# Create your models here.
