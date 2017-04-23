from django.conf.urls import patterns, include, url
from django.contrib import admin
import user

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^basicview/', include('user.urls')),

                       url(r'^auth/', include('loginsys.urls')),
                       url(r'^', include('user.urls')),
                       )