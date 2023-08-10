from celery import shared_task
from django.utils import timezone
from .models import ScheduledTask, Task

@shared_task
def schedule_tasks():
    now = timezone.now()
    scheduled_tasks = ScheduledTask.objects.filter(due_date__lte=now)

    for task in scheduled_tasks:
        Task.objects.create(
            title=task.title,
            description=task.description,
            assigned_to=task.assigned_to,
            status='pending',
        )
        task.delete()  

