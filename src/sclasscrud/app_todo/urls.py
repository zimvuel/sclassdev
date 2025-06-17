from django.urls import path
from app_todo.views import create, list, read, update, delete

urlpatterns = [
    path('create/', create.view, name='create'),
    path('list/', list.view, name='list'),
    path('read/<int:post_id>/', read.view, name='read'),
    path('update/<int:post_id>/', update.view, name='todo_update'),
    path('delete/<int:post_id>/', delete.view, name='todo_delete')
]