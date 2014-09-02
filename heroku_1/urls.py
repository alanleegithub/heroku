from django.conf.urls import patterns, include, url
from views import hello
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('blog.urls')),
    url(r'^blogs/', include('blog.urls')),
    url(r'^login/', 'blog.views.login'),
    url(r'^register/$', 'blog.views.register'),
    url(r'^hello/', hello),
    url(r'^admin/', include(admin.site.urls)),
)
