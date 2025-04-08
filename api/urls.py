from django.urls import path
from . import views


urlpatterns = [
    path('tasks/', views.task_list, name='task-list'),
    path('tasks/create/', views.task_create, name='task-create'),
    path('tasks/update/<int:id>/', views.task_update, name='task-update'),
    path('tasks/delete/<int:id>/', views.task_delete, name='task-delete'),
    path('tasks/<int:id>/', views.task_detail, name='task-detail'), 
]

