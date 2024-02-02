from django.contrib import admin
from .models import Sites

class SitesAdmin(admin.ModelAdmin):
    list_display = ('link', 'user_owner', 'status', 'updated_at')
    search_fields = ('link', 'user_owner')

admin.site.register(Sites, SitesAdmin)
# Register your models here.
