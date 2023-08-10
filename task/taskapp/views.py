from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Tasks,Employee_details


# @login_required
# def update_task_status(request, task_id):
#     task = get_object_or_404(Task, id=task_id, assigned_to=request.user.employee_details)
    
#     if request.method == 'POST':
#         new_status = request.POST['status']
#         task.status = new_status
#         task.save()
    
#     return redirect('task_list')



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list') 
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials.'})
    return render(request, 'login.html')

@login_required
def task_list(request):
    user = request.user 
    try:
        employee = Employee_details.objects.get(user=user) 
        tasks = Tasks.objects.filter(assigned_to=employee)
    except Employee_details.DoesNotExist:
        tasks = []  
    
    return render(request, 'task_list.html', {'tasks': tasks})

    
@login_required
def update_task_status(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)

    if request.method == 'POST':
        new_status = request.POST.get('new_status')
        task.status = new_status
        task.save()
        return redirect('task_list')

    return render(request, 'update_task_status.html', {'task': task})

