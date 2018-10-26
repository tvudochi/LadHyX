# coding=utf-8
from django.db import models
import datetime

# Create your models here.


# def heure():
#     myformat = "%H"
#     t = datetime.datetime(1970, 1, 1, 10, 0, 0)
#     h = t.hour
#     # s = h.strftime('%H:%M')
#     return h


class Evenement(models.Model):
    TYPE = (
        ('Séminaires', 'Séminaires'),
        # ('colloques', 'Colloques'),
        # ('Soutenances', 'Soutenances'),
        # ('Evenements', 'Evenements'),
    )
    LIEU = (
        ('LadHyX Library', 'LadHyX Library'),
        ('Lecture Hall, Turing building', 'Lecture Hall, Turing building'),
    )
    intitule_id = models.AutoField(primary_key=True)
    intitule = models.CharField(blank=False, max_length=255)
    type = models.CharField(max_length=100, choices=TYPE)
    domaine = models.CharField(blank=True, max_length=255)
    personne = models.CharField(blank=False, max_length=255)
    institut = models.CharField(blank=True, max_length=255)
    date_debut = models.DateField(auto_now=False, auto_now_add=False)
    date_fin = models.DateField(auto_now=False, auto_now_add=False)
    lieu = models.CharField(blank=True, max_length=255, choices=LIEU)
    heure = models.TimeField(blank=True, auto_now=False, auto_now_add=False, null=True)
    resume = models.TextField(blank=True)
    abstract = models.FileField(
        upload_to='evenement',
        blank=True,
        default=''
    )
    lien = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Evènement'
        verbose_name_plural = 'Evènement'

    def __str__(self):
        return self.intitule

