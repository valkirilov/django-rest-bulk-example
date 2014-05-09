from api.models import Teacher
from django.contrib import admin

    
class TeachersAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'degree', 'short', 'created', 'updated',)
    list_filter = ('name', 'degree', 'short', 'created', 'updated',)
    ordering = ('-created',)

admin.site.register(Teacher, TeachersAdmin)