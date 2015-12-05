from django.conf.urls import patterns, url

from rest_api.views import *

# test API is only for testing

urlpatterns = patterns('api_views',
                       url(r'^$', home, name='home'),
                       url(r'^test/$', test, name='test'),  # Testing Only
                       url(r'^order/$', order, name='order'),  # The rest api for orders

                       )
