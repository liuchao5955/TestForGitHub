from django.conf.urls import patterns, include, url
#from mysite.views import hello,current_datetime,hours_ahead,rq
from django.contrib import admin
from mysite import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello/$',views.hello),
    url(r'^time/$',views.current_datetime),
    url(r'^another-time-page/$',views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^rq/$',views.rq),
    url(r'^search-form/$',views.search_form),
    url(r'search/$',views.search),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^insert_Author/([^/]+)$',views.insert_Author),
    url(r'^getPostData$',views.getPostData),
    )
