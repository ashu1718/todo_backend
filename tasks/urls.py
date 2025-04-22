from django.urls import path
from . import views

urlpatterns = [
    path('tasks', views.task_list, name='task_list'),
    path('tasks/<uuid:pk>/complete', views.complete_task, name='complete_task'),
    path('tasks/<uuid:pk>/delete',views.delete_task,name='delete_task')
]
