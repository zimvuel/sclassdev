from django.shortcuts import render, redirect
from app_blog.utility import query

def view(request, post_id):
    if request.method == 'GET':
        post = query("DELETE from todolist WHERE id = %s", [post_id])
        print(post)
    return redirect('/todo/list')
