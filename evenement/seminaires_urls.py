from django.conf.urls import patterns, url

from evenement.views import seminaires

urlpatterns = patterns('',
                       # Examples:
                       #  url(r'^$', 'Personnel.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'', include('personnel.urls')),
                       url(r'^$', seminaires),
                       )
