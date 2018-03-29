from django.shortcuts import render
from django.http import JsonResponse
from .models import Todo

# Create your views here.

def todos_list(request):
  todos = []
  for todo in Todo.objects.all():
    todos += [
      {
        'id': todo.id,
        'name': todo.name,
        'isComplete': todo.is_complete
      }
    ]

  data = {'results': todos}
  response = JsonResponse(data)
  response['Content-Disposition'] = 'inline; filename=files.json'
  return response
