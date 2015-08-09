__author__ = 'ajrs'

from django.conf.urls import url, include, patterns

urlpatterns = patterns('',
                       url(r'^$', 'scrapbook.views.scrapbook'),
                       )
