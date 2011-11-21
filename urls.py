from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CircManager.views.home', name='home'),
    # url(r'^CircManager/', include('CircManager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^subscribe/', 'subs.views.index'),
    url(r'^upload/', 'uploader.views.index'),
    url(r'^upload_file/', 'uploader.views.upload_file'),
)
