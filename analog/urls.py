from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'analog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^document/',
        include('document.urls', namespace='document', app_name='document')),
    url(r'^admin/', include(admin.site.urls)),
)
