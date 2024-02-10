from django.contrib.auth.models import User
from django import forms
from .models import Sites

class EditLinkForm(forms.ModelForm):   
    class Meta:
        model = Sites
        fields = ('link',)
