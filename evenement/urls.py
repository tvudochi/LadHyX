# -*- coding: utf-8 -*-

from django.conf.urls import url

from evenement.views import news

urlpatterns = [
    url(r'^$', news, name="evenements"),
]

# http://127.0.0.1:8000/fr/les-membres/chercheurs/