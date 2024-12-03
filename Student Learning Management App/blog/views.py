from django.shortcuts import render, redirect
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})

def add_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category = request.POST['category']
        BlogPost.objects.create(title=title, content=content, category=category)
        return redirect('blog:blog_list')
    return render(request, 'blog/add_blog.html')
