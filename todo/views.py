from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm


def index(request):
    # main page controller
    todo_list = Todo.objects.order_by('id')
    form = TodoForm()

    context = {'todo_list': todo_list, 'form': form}
    return render(request, 'todo/index.html', context)


@require_POST
def addTodo(request):
    # adds a todo item
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()

    return redirect('index')


def deleteCompletedTask(request, todo_id):
    Todo.objects.get(pk=todo_id).delete()

    return redirect('index')


def deleteAllCompleted(request):
    Todo.objects.filter(completed__exact=True).delete()

    return redirect('index')


def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')
