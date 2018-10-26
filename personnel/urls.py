# -*- coding: utf-8 -*-

from django.conf.urls import url


from personnel.views import personnel, trombi

urlpatterns = [
    url(r'^$', personnel, name="membres"),
    url(r'^/trombi$', trombi, name="trombi"),
]

# http://127.0.0.1:8000/fr/les-membres/chercheurs/
