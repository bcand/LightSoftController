from django.conf.urls import patterns, url
from rest_api.views import *

urlpatterns = patterns('api_views',
        url(r'^$',home ,name='home' ),
        # url(r'^albums/$',rest_album , name='rest_rest_album'),

)