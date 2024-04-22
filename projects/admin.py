from django.contrib import admin
from .models import Project
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'locations', 'power', 'date']
    list_filter = ['date']
    search_fields = ['id']
admin.site.register(Project, ProjectAdmin)