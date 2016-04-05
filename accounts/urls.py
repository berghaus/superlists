from django.conf.urls import include, url
from django.contrib import admin
#from django.contrib.auth.views import logout as django_logout
from accounts import views as accounts_views

urlpatterns = [
    url(r'^login$', accounts_views.persona_login, name='persona_login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout' )
]
