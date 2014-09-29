from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from bank.views import account_view

urlpatterns = patterns('',
    url(r'^account/(?P<account_id>\w+)/$', account_view),
    url(r'^admin/', include(admin.site.urls)),
)
