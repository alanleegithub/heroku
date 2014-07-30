from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all/$', 'blog.views.blogs'),
    url(r'^get/(?P<post_id>\d+)/$', 'blog.views.blog'),
    url(r'^tag/(?P<tag>\w+)/$', 'blog.views.tagpage'),
)
