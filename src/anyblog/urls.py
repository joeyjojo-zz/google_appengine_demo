from django.conf.urls.defaults import *

urlpatterns = patterns('anyblog.views',
    url(r'^$', 'index'),
    url(r'^(?P<blogpost_id>\d+)/$', 'detail'),
    url(r'^(\d{4})/(\d{2})/$', 'month_archive')
)
