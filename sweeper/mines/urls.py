from django.conf.urls import patterns, url

urlpatterns = patterns('mines.views',
    url(r'^randomize/(?P<num_cells>[0-9]+)/(?P<num_mines>[0-9]+)/$','randomize'),
)
