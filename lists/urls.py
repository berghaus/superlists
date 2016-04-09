from django.conf.urls import include, url
from django.contrib import admin
from lists import views as lists_views

urlpatterns = [
    url(r'^(\d+)/$', lists_views.view_list, name='view_list'),
    url(r'^new$', lists_views.new_list, name='new_list'),
    url(r'^users/(.+)/$', lists_views.my_lists, name='my_lists'),
]
