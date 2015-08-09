__author__ = 'ajrs'

from django.conf.urls import url, include, patterns
import projects.views as views

urlpatterns = patterns('',
                       url(r'^$', 'projects.views.projects'),
                       )