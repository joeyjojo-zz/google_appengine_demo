from django.conf.urls.defaults import *

urlpatterns = patterns('anyblog.views',
    url(r'^$', 'index'),
    url(r'^(?P<blogpost_id>\d+)/$', 'detail'),
)
