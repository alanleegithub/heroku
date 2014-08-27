#from django.shortcuts import render
# Create your views here.

from django.shortcuts import render_to_response
from blog.models import Post
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth

def blogs(request):
    return render_to_response('blogs.html',
        {'blogs': Post.objects.all()},  context_instance=RequestContext(request))

def blog(request, post_id = 1):
    return render_to_response('blog.html',
        {'post': Post.objects.get(id = post_id)})

def tagpage(request, tag):
    posts = Post.objects.filter(tags__name = tag)
    return render_to_response('tagpage.html',
        {'posts': posts, 'tag': tag})

from django.contrib.auth.forms import UserCreationForm

def login(request):
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(email=email, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('blogs.html')
    else:
        return HttpResponseRedirect('/register/main/')

def register_main(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('register.html',  c)

def register_check(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blogs/')
        else:
            return HttpResponseRedirect('/register/main/')

def register_success(request):
    return render_to_response('register_success.html')
