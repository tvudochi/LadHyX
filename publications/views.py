# -*- coding: utf-8 -*-
import subprocess
import csv
import re
from django.conf import settings
from django.shortcuts import render, redirect
from datetime import date
from collections import OrderedDict
from publications.forms import SearchForm
from django.http import HttpResponseRedirect

# search-pub-rp-stdin.exe <annee> Au<auteur> <editeur>
# all si var = 0
# Pour chaque anne : search(request, annee, Auauteur=0, editeur=0)
# Pour la balise select
# search(request,annee=0, Auauteur, editeur=0)
# search(request,annee=0, Auauteur=0, editeur)
# search(request,annee=0, Auauteur=0, editeur=0)


def searchpublis(request, annee=None, auteur=0, editeur=0):
    if request.method == 'GET':
        prog = settings.PROG
        print(prog)
        result = subprocess.Popen(
            [prog, str(annee), str(auteur), str(editeur)],
            stdout=subprocess.PIPE,
            shell=False, bufsize=1400000)
        stdout_value = result.communicate()[0].decode("iso8859-15")
        mylist = stdout_value.splitlines()
        mylistfinal = []
        for j in mylist:
            l = j.replace('&nbsp;', ' ', 100)
            mylistfinal.append(l)

        mycsv = csv.DictReader(mylistfinal, delimiter='+',
                               fieldnames=[
                                   'date',
                                   'auteurs',
                                   'titre',
                                   'journal',
                                   'index',
                                   'abstract',
                                   'preprint'
                               ])

        maliste = list(mycsv)
        # mycsv : <class 'csv.DictReader'>
        # on itère sur mycsv, chaque itération donne une dict.
        # maliste liste de dict
        return render(request, 'searchpublications.html',
                      {
                          "maliste": maliste,
                      }
                      )


def searchform(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data['auteur'])
            # print(form.cleaned_data['journal'])
            auteur = form.cleaned_data['auteur']
            editeur = form.cleaned_data['journal']
            myauteur = auteur.replace('Wa', 'Au', 1)
            prog = settings.PROG
            result = subprocess.Popen(
                [prog, '0', str(myauteur), str(editeur)],
                stdout=subprocess.PIPE,
                shell=False, bufsize=1400000)
            stdout_value = result.communicate()[0].decode("iso8859-15")
            mylist = stdout_value.splitlines()
            mylistfinal = []
            for j in mylist:
                l = j.replace('&nbsp;', ' ',100)
                mylistfinal.append(l)

            mycsv = csv.DictReader(mylistfinal, delimiter='+',
                                   fieldnames=[
                                       'date',
                                       'auteurs',
                                       'titre',
                                       'journal',
                                       'index',
                                       'abstract',
                                       'preprint'
                                   ])

            maliste = list(mycsv)

            # mycsv : <class 'csv.DictReader'>
            # on itère sur mycsv, chaque itération donne une dict.
            # maliste liste de dict
            return render(request, 'searchpublications.html',
                          {
                              "maliste": maliste,
                          }
                          )
            # return redirect('www.google.fr')
        else:
            print('form pas valide')
    else:
        form = SearchForm()


    return render(request, 'publications.html',
                      {
                          "form": form,
                      }
                      )


def searchouvrages(request, annee, auteur=0, editeur=0):
    with open(settings.OUVRAGES, 'r', encoding='iso8859-15') as myfile:
        reg = '^'+annee
        mylist = []
        for line in myfile:
            if re.search(reg, line):
                mylist.append(line)

        mycsv = csv.DictReader(mylist, delimiter='|',
                               fieldnames=[
                                   'date',
                                   'auteurs',
                                   'titre',
                                   'editeur',
                                   'references',
                                   'abstract',
                                   'preprint'
                               ])

        maliste = list(mycsv)
        return render(request, 'searchouvrages.html',
                      {
                          "maliste": maliste,
                      }
                      )


def searchtheses(request, annee=None, auteur=0, editeur=0):
    with open(settings.THESES, 'r', encoding='iso8859-15') as myfile:

        reg = '^'+annee
        mylist = []
        for line in myfile:
            if re.search(reg, line):
                mylist.append(line)

        mycsv = csv.DictReader(mylist, delimiter='|',
                               fieldnames=[
                                   'date',
                                   'auteur',
                                   'titre',
                                   'references',
                                   'directeurs',
                                   'pdf',
                               ])
        maliste = list(mycsv)

    return render(request, 'searchtheses.html',
                      {
                          "maliste": maliste,
                      }
                      )


def allpublis(request):

    if request.method == 'GET':

        today = date.today()
        prog = settings.BASE_DIR + '/publications/Prog/search-pub-rp-stdin'
        mydict = OrderedDict()
        for i in range(today.year, 1989, -1):
            result = subprocess.Popen(
                [prog, str(i), "0", "0"],
                stdout=subprocess.PIPE,
                shell=False, bufsize=1400000)
            stdout_value = result.communicate()[0].decode("iso8859-15")
            mylist = stdout_value.splitlines()
            mycsv = csv.DictReader(mylist, delimiter='+',
                                   fieldnames=[
                                       'date',
                                       'auteurs',
                                       'titre',
                                       'journal',
                                       'index',
                                       'abstract',
                                       'preprint'
                                   ])
            maliste = list(mycsv)
            mydict[i] = maliste

        # mydict dict dont les clefs sont les années
        # mydict[annee] liste de publications

        # mycsv : <class 'csv.DictReader'>
        # on itère sur mycsv, chaque itération donne une dict.
        # maliste liste de dict
        return render(request, 'publications.html',
                        {
                            "maliste": mydict,
                         }
                      )




