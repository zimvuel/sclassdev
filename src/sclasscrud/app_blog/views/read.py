from django.shortcuts import render
from app_blog.utility import query

def view(request, post_id):
    if request.method == 'GET':
        post = query("SELECT * from blog_post WHERE id = %s", [post_id])
        if post:
            return render(request, 'app_blog/read.html', {'post':post[0]})
    return render(request, 'app_blog/notfound.html', status=404)
