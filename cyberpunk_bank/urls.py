from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from rest_framework import viewsets, routers

from bank.models import Account

class AccountViewSet(viewsets.ModelViewSet):
    model = Account

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cyberpunk_bank.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
