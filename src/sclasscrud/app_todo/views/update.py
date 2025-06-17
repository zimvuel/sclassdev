from django.shortcuts import render, redirect
from app_blog.utility import query

def view(request, post_id):
    post = query("SELECT * from todolist WHERE id = %s", [post_id])
    print(post)

    if request.method == "GET":
        return render(request, 'app_todo/update.html', {'post':post[0]})

    if not post:
        return render(request, 'app_todo/notfound.html', status=404)
    if request.method == 'POST':
        post = post[0]
        title = request.POST.get('title')
        content = request.POST.get('content')
        result = query("UPDATE todolist SET title = %s, content = %s WHERE id = %s", [title, content, post_id]) #
        print(result)
        return redirect(f"/todo/read/{post_id}")

