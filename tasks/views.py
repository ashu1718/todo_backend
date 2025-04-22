from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from .models import Task
from .serializers import TaskSerializer
import json

# Helper to check and update task statuses
def update_task_status(task):
    if task.status == 'ongoing' and now() > task.deadline:
        task.status = 'failure'
        task.save()
    return task

@csrf_exempt
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        for task in tasks:
            update_task_status(task)
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def complete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

    if request.method == 'POST':
        if now() <= task.deadline:
            task.status = 'success'
            task.save()
        else:
            update_task_status(task)
        return JsonResponse({'status': task.status})


@csrf_exempt
def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

    if request.method == 'DELETE':
        task.delete()
        return JsonResponse({'message': 'Task deleted'})
