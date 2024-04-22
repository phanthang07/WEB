from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'locations', 'contact']
    list_filter = ['name']
    search_fields = ['name']
admin.site.register(Customer, CustomerAdmin)
