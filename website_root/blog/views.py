from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-posted_at')[:5]
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

def new_post(request):
    return render(request, 'blog/new_post.html')

def publish(request):
    new_post = Post(title=request.POST['title'], content=request.POST['content'])
    new_post.save()
    return redirect('blog:index')

def details(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {
        'post': post
    }
    return render(request, 'blog/post_details.html', context)