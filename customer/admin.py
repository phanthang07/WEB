from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customercode', 'customertype', 'name', 'locations',]
    list_filter = ['name']
    search_fields = ['name']
admin.site.register(Customer, CustomerAdmin)
