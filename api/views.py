from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.decorators import login_required
from rest_framework import status
from django.http import JsonResponse, Http404 , HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import json

@csrf_exempt
def task_list(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            tasks = Task.objects.filter(user=request.user).values()
        else:
            tasks = Task.objects.all().values()  # Show all tasks (read-only)
        return JsonResponse(list(tasks), safe=False)

    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Unauthorized. Login to add tasks.'}, status=401)

        try:
            data = json.loads(request.body)
            task = Task.objects.create(
                title=data.get('title'),
                description=data.get('description', ''),
                user=request.user
            )
            return JsonResponse({
                'id': task.id,
                'title': task.title,
                'description': task.description
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


@api_view(['POST'])
def task_create(request):
    data = request.data.copy()
    data['user'] = request.user.id
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@csrf_exempt
def task_update(request, id):  # 👈 Make sure 'id' is accepted here
    if request.method == 'PUT':
        try:
            task = Task.objects.get(id=id)
            data = json.loads(request.body)

            task.title = data.get('title', task.title)
            task.description = data.get('description', task.description)
            task.status = data.get('status', task.status)
            task.priority = data.get('priority', task.priority)
            task.due_date = data.get('due_date', task.due_date)
            task.save()

            return JsonResponse({'message': 'Task updated successfully'})
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)
    return HttpResponseBadRequest("Invalid method")

@api_view(['DELETE'])
def task_delete(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    task.delete()
    return Response({'message': 'Task deleted'})




def task_detail(request, id):
    if request.method == 'GET':
        try:
            task = Task.objects.get(id=id)
            return JsonResponse({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'status': task.status,
                'priority': task.priority,
                'due_date': task.due_date
            })
        except Task.DoesNotExist:
            raise Http404("Task not found")

