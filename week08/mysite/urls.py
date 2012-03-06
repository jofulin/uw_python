from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

# This also imports the include function
from django.conf.urls.defaults import *

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^books/', include('books.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

