from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'firstapp.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^1/', 'user.views.basic_one'),
                       url(r'^2/', 'user.views.template_two'),
                       url(r'^3/', 'user.views.template_three_simple'),
                       url(r'^users/all/$', 'user.views.users'),
                       url(r'^users/get/(?P<article_id>\d+)/$', 'user.views.user'),
                       url(r'^users/addlike/(?P<article_id>\d+)/$', 'user.views.addlike'),
                       url(r'^users/addcomment/(?P<article_id>\d+)/$', 'user.views.addcomment'),
                       url(r'^page/(\d+)/$', 'user.views.users'),
                       url(r'^', 'user.views.users'),

                       )
