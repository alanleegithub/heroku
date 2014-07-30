#from django.shortcuts import render
# Create your views here.

from django.shortcuts import render_to_response
from blog.models import Post

def blogs(request):
    return render_to_response('blogs.html',
        {'blogs': Post.objects.all()})

def blog(request, post_id = 1):
    return render_to_response('blog.html',
        {'post': Post.objects.get(id = post_id)})

def tagpage(request, tag):
    posts = Post.objects.filter(tags__name = tag)
    return render_to_response('tagpage.html',
        {'posts': posts, 'tag': tag})
