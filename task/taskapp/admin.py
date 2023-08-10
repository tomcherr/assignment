from django.contrib import admin
from .models import Employee_details, Tasks

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    
admin.site.register(Employee_details, EmployeeAdmin)

from django import forms

class TaskStatusForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['status']
        widgets = {
            'status': forms.Select,  # Use a dropdown widget for status field
        }
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'assigned_to', 'status')
    form = TaskStatusForm 

admin.site.register(Tasks, TaskAdmin)

