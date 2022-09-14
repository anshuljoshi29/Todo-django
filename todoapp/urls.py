from . import views
from django.urls import path

urlpatterns = [
    path('',views.watch,name='watch'),
    path('todoapp/',views.todoappView,name='todoview'),
    path('addTodoItem/',views.addTodoView,name='todoadd'),
    path('deleteTodoItem/<int:i>/',views.deleteTodoView,name='deletetodo'),
]
