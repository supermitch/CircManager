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

    url(r'^$', 'index.views.index', name='home'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    # Custom views
    url(r'^subscribe/', 'subs.views.index'),
    url(r'^upload/', 'uploader.views.upload_file', name='upload'),
    url(r'^success/', 'uploader.views.success', name='success'),

    #ToDo urls
   # would like to redirect to a "results/" url instead of to nothing...
   # url(r'^results/', 'uploader.views.results', name='results'),
)
