from django.shortcuts import render
from app_blog.utility import query

def view(request):

    if request.method == 'GET':
        posts = query("SELECT * from todolist ORDER BY id DESC")
    return render(request, 'app_todo/list.html', {
        'posts' : posts
    })