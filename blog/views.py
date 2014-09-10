#from django.shortcuts import render
# Create your views here.

from django.shortcuts import render_to_response
from blog.models import Post, Comment
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth
from forms import MyRegistrationForm
from forms import PostForm, CommentForm
from django.shortcuts import render

def blogs(request):
    if request.user.is_authenticated():
       if request.user.username == 'alanlee' or request.user.username == 'admin':
          page = 'blogs_admin.html'
       else:
          page = 'blogs_login.html'
       return render_to_response(page,
           {'blogs': Post.objects.all().order_by('-published_date'), 
            'user': request.user})
    else:
       return render_to_response('blogs.html',
           {'blogs': Post.objects.all().order_by('-published_date')},  context_instance=RequestContext(request))

def blog(request, post_id = 1):
    if request.user.is_authenticated():
       if request.user.username == 'alanlee' or request.user.username == 'admin':
          page = 'blog_admin.html'
       else:
          page = 'blog_login.html'
       return render_to_response(page,
           {'post': Post.objects.get(id = post_id),
            'user': request.user})
    else:
       return render_to_response('blog.html',
           {'post': Post.objects.get(id = post_id)})

def tagpage(request, tag):
    posts = Post.objects.filter(tags__name = tag)
    return render_to_response('tagpage.html',
        {'posts': posts, 'tag': tag})

from django.contrib.auth.forms import UserCreationForm

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/blogs/')
    return HttpResponseRedirect('/register/')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def post(request):
    if request.method == 'POST':
       form = PostForm(request.POST)
       if form.is_valid():
          f = form.save(commit = False)
          f.author = request.user
          f.save()
          return HttpResponseRedirect('/blogs/')
    else:
       form = PostForm()
    return render_to_response('blog_post.html',
        {'user': request.user,
         'form': form},  context_instance=RequestContext(request))

def register(request):
    # 2nd time around
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect('/blogs/')
        return render(request, 'register.html', {'form': form})

    # 1st time visit
    args = {}
    args.update(csrf(request))
    # form with no input
    args['form'] = MyRegistrationForm()
    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')

def about(request):
    return render_to_response('about.html')

def comment(request, post_id = 1):
    if request.method == 'POST':
       form = CommentForm(request.POST)
       if form.is_valid():
          f = form.save(commit = False)
          f.author = request.user
          f.post_id = post_id
          f.save()
          return HttpResponseRedirect('/blogs/')
    else:
       form = CommentForm()
    return render_to_response('blog_comments.html',
           {'comments': Comment.objects.filter(post_id = post_id).order_by('-published_date'),
            'user': request.user,
            'form': form,
            'blog_id': post_id},  context_instance=RequestContext(request))
