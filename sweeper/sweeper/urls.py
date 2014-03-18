from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^mines/', include('mines.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^game/', include('frontend.urls')),
)
