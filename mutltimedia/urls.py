# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.conf.urls import url
from mutltimedia.views import requestvimeo

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


    url(r'^experiences-enseignement$',
        requestvimeo,
        {'channel': '1271461', 'name': 'expériences d\'enseignement'},
        name="experiences-enseignement"),

    url(r'^ingenierie-du-vent-aeroelasticite$',
        requestvimeo,
        {'channel': 'aeroelasticite', 'name': 'ingénierie du vent et aéroélasticité'},
        name="ingenierie-du-vent-aeroelasticite"),

    url(r'^physique-du-sport$',
        requestvimeo,
        {'channel': '1271458', 'name': 'Physique du sport'},
        name="physiquedusport"),

    url(r'^mecanique-cellulaire$',
        requestvimeo,
        {'channel': '1271457', 'name': 'mecanique cellulaire'},
        name="mecanique-cellulaire"),

    url(r'^art-et-science$',
        requestvimeo,
        {'channel': '1270487', 'name': 'art et science'},
        name="artetscience"),

]
