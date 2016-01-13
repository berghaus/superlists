from django.conf.urls import include, url
from django.contrib import admin
from lists import views as lists_views

urlpatterns = [
    # Examples:
    url(r'^$', lists_views.home_page, name='home'),
    url(r'^lists/the-only-list-in-the-world/$', lists_views.view_list, name='view_list'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
]
