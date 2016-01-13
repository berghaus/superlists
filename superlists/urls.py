from django.conf.urls import include, url
from django.contrib import admin
from lists import views as lists_views

urlpatterns = [
    # Examples:
    url(r'^$', lists_views.home_page, name='home'),
    url(r'^lists/(\d+)/$', lists_views.view_list, name='view_list'),
    url(r'^lists/(\d+)/add_item$', lists_views.add_item, name='add_item'),
    url(r'^lists/new$', lists_views.new_list, name='new_list'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
]
