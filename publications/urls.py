# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.conf.urls import url
from publications.views import searchpublis, searchouvrages, searchtheses, searchform

# /publications
# /publications/revues/<year>
# /publications/ouvrages/<year>
# /publications/theses/<year>
# /publications/form --> redirect.
# search <annee> <Auauteur> <Editeur>
# publications/revues-comite-de-lecture/<annee>
# search <annee> 0 0
# publications/revues-comite-de-lecture/
# search 0 <Auauteur> 0 / Par auteur
# search 0 0 <Editeur> / Par Editeur
# search 0 0 0 / Tout

urlpatterns = [
    # url(r'^$',
    #     TemplateView.as_view(template_name="publications.html"),
    #     name="publications"),

    url(r'^$',
        searchform,
        name="publications"),

    url(r'^revues/(?P<annee>\d{4})/$',
        searchpublis,
        {'auteur': '0', 'editeur': '0'},
        name="searchpublications"),

    url(r'^ouvrages/(?P<annee>\d{4})/$',
        searchouvrages,
        {'auteur': '0', 'editeur': '0'},
        name="searchouvrages"),

    url(r'^theses/(?P<annee>\d{4})/$',
        searchtheses,
        {'auteur': '0', 'editeur': '0'},
        name="searchtheses"),
]
