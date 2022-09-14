from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import todoList
    
def todoappView(request):
    values= todoList.objects.all()
    return render(request, 'index.html',
    {'data':values})

def addTodoView(request):
    x = request.POST['content']
    new_item = todoList(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    y =todoList.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')