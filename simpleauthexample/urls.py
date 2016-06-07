from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.contrib import admin



urlpatterns = patterns('',
   url(r'^login/', 'simpleauthexample.views.loginview'),
   url(r'^auth/', 'simpleauthexample.views.auth_and_login'),
   url(r'^signup/', 'simpleauthexample.views.sign_up_in'),
   url(r'^impersonate/(?P<user_id>[0-9]+)', 'simpleauthexample.views.impersonate'),
   url(r'^$', 'simpleauthexample.views.secured'),
   url(r'^admin/', admin.site.urls),
)
