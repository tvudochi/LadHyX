# -*- coding: utf-8 -*-
from django.shortcuts import render
from evenement.models import Evenement
from django.views.generic.base import TemplateView

# from django.db.models import Q

import datetime


class Accueil(TemplateView):

    template_name = "accueil.html"

    def get_context_data(self, **kwargs):
        context = super(Accueil, self).get_context_data(**kwargs)
        # Date du jour
        now = datetime.datetime.now()
        # Requête  sur tous les objets ayant une date supérieure à celle du
        # jour
        queryset_news = Evenement.objects.filter(date_fin__gte=now)
        # Tri de la liste obtenue par date
        list_sorted = sorted(queryset_news, key=lambda r: r.date_debut)
        print(queryset_news)
        if list_sorted:
            context['leprochain'] = list_sorted[0]
        if not list_sorted:
            context['leprochain'] = []
        return context
