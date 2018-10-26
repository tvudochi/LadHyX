# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
import csv
import re
from django.utils.translation import ugettext as _

# from publications.views import liste_auteurs


def liste_auteurs():
    with open(settings.INFO, "r", encoding="iso8859-15") as infofile:
        reg = "^Wa"
        mylist = []
        for line in infofile:
            if re.search(reg, line):
                # enco = line.encode('utf-8')
                mylist.append(line.rstrip('\n'))

        reader = csv.DictReader(mylist, delimiter='|',
                                fieldnames=[
                                    'Code',
                                    'Nom_C',
                                    'Nom_D'
                                ]
                                )
        liste = [(0, 'Auteur')]
        for row in reader:
            # print(row['Code'], row['Auteur'])
            person = (row['Code'], row['Nom_C'])
            liste.append(person)

        mytuple = tuple(liste)
        return mytuple


def liste_editeurs():
    with open(settings.INFO, "r", encoding="iso8859-15") as infofile:
        reg = "^Ed"
        mylist = []
        for line in infofile:
            if re.search(reg, line):
                if re.match('Ed0', line):
                    pass
                else:
                    mylist.append(line.rstrip('\n'))

        reader = csv.DictReader(mylist, delimiter='|',
                                fieldnames=[
                                    'Code',
                                    'Nom',
                                ]
                                )
        liste = [(0, 'Journal')]
        for row in reader:
            # print(row['Code'], row['Auteur'])
            journal = (row['Code'], row['Nom'])
            liste.append(journal)

        mytuple = tuple(liste)
        return mytuple


class SearchForm(forms.Form):
    CHOICES = (('Option 1', 'Option 1'), ('Option 2', 'Option 2'),)

    auteur = forms.ChoiceField(required=False, label=_('Auteur'),
                             # widget=forms.TextInput(attrs={'placeholder': 'Auteur'}),
                             # select=forms.Select(choices=CHOICES)
                               choices=liste_auteurs()
                             )
    journal = forms.ChoiceField(label='Journal', required=False,
                              # widget=forms.TextInput(attrs={'placeholder': 'Journal'}),
                                choices=liste_editeurs(),
                              )

