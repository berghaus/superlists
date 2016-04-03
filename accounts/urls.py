from django.conf.urls import include, url
from accounts import views as accounts_views

urlpatterns = [
    url(r'^login', accounts_views.login, name='login'),
    url(r'^logout', accounts_views.logout, name='logout'),
]
