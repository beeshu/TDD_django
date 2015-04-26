from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^(\d+)/$', 'lists.views.view_list', name='view_list'),
    url(r'^new$', 'lists.views.new_list', name='new_list'),
    url(r'^json_home$', 'lists.views.view_json_home', name='view_json_home'),
    url(r'^json_test$', 'lists.views.json_test', name='json_test'),
)
