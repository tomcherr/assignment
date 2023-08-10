from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Employee_details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('employee', 'Employee')])


class Tasks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(Employee_details, on_delete=models.CASCADE)

    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    def __str__(self):
        return self.title

class ScheduledTask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(Employee_details, on_delete=models.CASCADE)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title
