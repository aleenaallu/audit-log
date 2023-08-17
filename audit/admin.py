from django.contrib import admin

# Register your models here.
from .models import *
from django.apps import apps

# apps = apps.get_app_config('audit')

# for model_name, model in apps.models.items():
#     admin.site.register(model)
    
    
class APICallAdmin(admin.ModelAdmin):
    list_display = ('user', 'endpoint', 'method', 'timestamp', 'ip_address')
    list_filter = ('user', 'method', 'timestamp')
    search_fields = ('user__username', 'endpoint', 'ip_address')

admin.site.register(APICall, APICallAdmin)
