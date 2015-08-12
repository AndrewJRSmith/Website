__author__ = 'ajrs'

from django.conf.urls import url, include, patterns
import projects.views as views

urlpatterns = patterns('',
                       url(r'^$', 'projects.views.projects'),
                       url(r'^more_info/(?P<more_info_page>[\w\-]+)/$', 'projects.views.more_info'),
                       )
