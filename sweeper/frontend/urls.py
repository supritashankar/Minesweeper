from django.conf.urls import patterns, url

urlpatterns = patterns('frontend.views',
    url(r'^newgame','newgame'),
    url(r'^(?P<level>B|I|E)/$','display_mine'),
)
