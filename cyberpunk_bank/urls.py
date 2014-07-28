from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from bank.views import account_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cyberpunk_bank.views.home', name='home'),
    url(r'^account/(?P<account_number>[0-99]+)/$', account_view),
    url(r'^admin/', include(admin.site.urls)),
)
