"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       # url(r'^about/', include('basic_pages.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^about/$', 'basic_pages.views.about'),
                       url(r'^contact/$', 'basic_pages.views.contact'),
                       url(r'^music/$', 'basic_pages.views.music'),
                       url(r'^projects/$', include('projects.urls')),
                       url(r'^scrapbook/$', include('scrapbook.urls')),
                       url(r'^structuralengineering/$', 'basic_pages.views.structuralengineering'),
                       url(r'^$', 'basic_pages.views.index'),
                       )
