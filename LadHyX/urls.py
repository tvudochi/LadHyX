"""LadHyX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext as _
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from LadHyX.views import Accueil

# from actualites.views import news

urlpatterns = i18n_patterns(

    url(r'^admin/', admin.site.urls),

    # Accueil et la recherche
    # url(r'^$',
    #     TemplateView.as_view(template_name="accueil.html"),
    #    name="accueil"),
    url(r'^$', Accueil.as_view(), name='accueil'),

    url(r'^evenements/', include('evenement.urls')),

    url(r'^actualites',
        TemplateView.as_view(template_name="actualites.html"),
        name="actualites"),

    url(r'recherche/', include('LadHyX.larecherche_urls')),

    # Les membres
    url(r'^membres',
        include('personnel.urls')),

    # Les publications
    url(r'^publications/',
        include('publications.urls')),

    url(r'^multimedia$',
        TemplateView.as_view(template_name="multimedia.html"),
        name="multimedia"),

    url(r'multimedia/', include('mutltimedia.urls')),

    # url(r'^partenariats$',
    #     TemplateView.as_view(template_name="partenariats.html"),
    #     name="partenariats"),


    url(r'^recrutements',
        TemplateView.as_view(template_name="recrutements.html"),
        name="recrutements"),

    url(r'^mentions-legales$',
        TemplateView.as_view(template_name="mentions-legales.html"),
        name="mentions-legales"),

    url(r'^a-propos$',
        TemplateView.as_view(template_name="a-propos.html"),
        name="a-propos"),

    url(r'^acces$',
        TemplateView.as_view(template_name="acces.html"),
        name="acces"),
    url(r'^trombi',
        TemplateView.as_view(template_name="trombi.html"),
        name="trombi"),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
