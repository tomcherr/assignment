from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Employee_details, Tasks

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    
admin.site.register(Employee_details, EmployeeAdmin)
# admin.site.register(Tasks)
# employees/admin.py

# employees/admin.py
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

# from django.contrib import admin
# from django.utils import timezone
# from .models import Employee_details, Task
# from .tasks import process_upcoming_tasks

# class TaskAdmin(admin.ModelAdmin):
#     actions = ['process_selected_tasks']

#     def process_selected_tasks(self, request, queryset):
#         now = timezone.now()
#         tasks_due_soon = queryset.filter(due_date__gte=now, due_date__lte=now + timedelta(days=1))
        
#         for task in tasks_due_soon:
#             process_upcoming_tasks.delay()  # Delayed execution of the Celery task

#         self.message_user(request, f'Successfully triggered processing for {tasks_due_soon.count()} tasks.')

#     process_selected_tasks.short_description = "Process selected tasks"

# admin.site.register(Employee_details)
# admin.site.register(Tasks, TaskAdmin)
