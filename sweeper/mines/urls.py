from django.conf.urls import patterns, url

urlpatterns = patterns('mines.views',
    url(r'^randomize/(?P<n>[3|6|9])+','randomize'),
)
