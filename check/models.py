from django.db import models
from django.contrib import admin
    
class Sites(models.Model):
    link = models.URLField(max_length=200)
    userId = models.CharField(max_length=100)
    @admin.display(
        boolean= True,
        ordering='userId',
        description='strony internetowe',
    )
    def __str__(self):
        return self.link
    
# Create your models here.
