from django.shortcuts import render
from app_todo.utility import query

def view(request, post_id):
    if request.method == 'GET':
        post = query("SELECT * from todolist WHERE id = %s", [post_id])
        if post:
            return render(request, 'app_todo/read.html', {'post':post[0]})
    return render(request, 'app_todo/notfound.html', status=404)
