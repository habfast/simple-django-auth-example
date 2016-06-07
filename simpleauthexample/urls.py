from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.contrib import admin
from . import views

urlpatterns = patterns(
    '',
    url(r'^login/', views.loginview),
    url(r'^auth/', views.auth_and_login),
    url(r'^signup/', views.sign_up_in),
    url(r'^impersonate/(?P<user_id>[0-9]+)', views.impersonate),
    url(r'^$', views.secured),
    url(r'^admin/', admin.site.urls),
)
