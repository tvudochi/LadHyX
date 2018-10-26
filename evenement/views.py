# -*- coding: utf-8 -*-
from django.shortcuts import render
from evenement.models import Evenement
# from django.db.models import Q

import datetime


def news(request):

    if request.method == 'GET':
        # Date du jour
        now = datetime.datetime.now()
        # Requête  sur tous les objets ayant une date supérieure à celle du
        # jour
        queryset_news = Evenement.objects.filter(date_fin__gte=now)
        # print(type(queryset_news[0].date_debut))
        # Tri de la liste obtenue par date
        list_sorted = sorted(queryset_news, key=lambda r: r.date_debut)
        # print(list_sorted[0:2])
        # Les deux premiers d'abord puis le reste dans le modal du template
        return render(request,
                      'evenement.html',
                      {
                          "leprochain": list_sorted[0:1],
                          "2first": list_sorted[0:2],
                          "lereste": list_sorted[2:]
                      }
                      )


def accueil(request):

    if request.method == 'GET':
        # Date du jour
        now = datetime.datetime.now()
        # Requête  sur tous les objets ayant une date supérieure à celle du
        # jour
        queryset_news = Evenement.objects.filter(date_fin__gte=now)
        # print(type(queryset_news[0].date_debut))
        # Tri de la liste obtenue par date
        list_sorted = sorted(queryset_news, key=lambda r: r.date_debut)
        # print(list_sorted[0:2])
        # Les deux premiers d'abord puis le reste dans le modal du template
        return render(request,
                      'accueil.html',
                      {
                          "leprochain": list_sorted[0:1],
                          "2first": list_sorted[0:2],
                          "lereste": list_sorted[2:]
                      }
                      )