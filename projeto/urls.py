from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'pessoas.views.index'),
	url(r'^validar/$', 'pessoas.views.validar'),
)
