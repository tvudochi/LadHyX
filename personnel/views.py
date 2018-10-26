# coding=utf-8
from django.shortcuts import render
from personnel.models import Personnel


# Thematique_technique, Thematique_societale

# Create your views here.
# Par thématique sociétale : Chercheurs permanents et encadrés.
# ITA
# Liste des ITA, Chercheurs, Doctorants, Post-docs
# liste
# select nom, prenom, page_perso, photo  from personnel_personnel where
# categorie = <Chaine>;
# Chaine = ITA, Chercheur, Doctorant, Post-doc,Anciens (page à part)
# daniel=Personnel.objects.all().filter(categorie='ITA')[0]
# daniel.nom

# Revoir le code des 4 fonctions 'liste' afin de les mutualiser.
# --> Pb d'intégration des urls dans le CMS.

# you can use the divisibleby tag as mentioned before, but for template clearing purposes I usually prefer a helper function that returns a generator:
#
# def grouped(l, n):
#     for i in xrange(0, len(l), n):
#         yield l[i:i+n]
# example simplistic view:
#
# from app.helpers import grouped
#
# def foo(request):
#     context['object_list'] = grouped(Bar.objects.all(), 4)
#     return render_to_response('index.html', context)
# example template:
#
# {% for group in object_list %}
#    <ul>
#         {% for object in group %}
#             <li>{{ object }}</li>
#         {% endfor %}
#    </ul>
# {% endfor %}

def chercheur(request):
    if request.method == 'GET':
        # chercheurs = Personnel.objects.extra(
        #     select={'nom':'UPPER(nom)'},
        #     order_by=['nom'],
        #     where=["categorie=Chercheur"],
        # )

        chercheurs_avec_photos = Personnel.objects.all().filter(
            categorie="Chercheur").filter(Photo__regex='\w+').filter(presence=True).order_by('nom')

        chercheurs_all = Personnel.objects.all().filter(
            categorie="Chercheur").filter(presence=True).order_by('nom')

        return render(request, 'chercheur.html',
                      {"chercheurs_avec_photos": chercheurs_avec_photos,
                       "chercheurs_all": chercheurs_all,
                       }
                      )


def ita(request):
    if request.method == 'GET':
        ita_all = Personnel.objects.all().filter(
            categorie="ITA").filter(presence=True).order_by('nom')
        ita_avec_photos = Personnel.objects.all().filter(
            categorie="ITA").filter(Photo__regex='\w+').filter(presence=True).order_by('nom')
        return render(request, 'membres.html',
                      {
                          "ita_all": ita_all,
                          "ita_avec_photos": ita_avec_photos,
                      }
                      )


def doctorant(request):
    if request.method == 'GET':
        doctorants = Personnel.objects.all().filter(
            categorie="Doctorant").filter(presence=True).order_by('nom')
        return render(request, 'doctorant.html',
                      {"people": doctorants, }
                      )


def postdoc(request):
    if request.method == 'GET':
        postdocs = Personnel.objects.all().filter(
            categorie="Post-doc").filter(presence=True).order_by('nom')
        return render(request, 'postdoc.html',
                      {"people": postdocs, }
                      )


# App pour gérer les anciens LadHyX.


def ancien(request):
    if request.method == 'GET':
        all = Personnel.objects.all()
        chercheurs = all.filter(categorie='Chercheur').filter(
            presence=False).order_by('nom')
        ita = all.filter(categorie='ITA').filter(
            presence=False).order_by('nom')
        doctorants = all.filter(categorie='Doctorant').filter(
            presence=False).order_by('nom')
        postdocs = all.filter(
            categorie='Post-doc').filter(presence=False).order_by('nom')
        return render(request, 'anciens.html',
                      {
                          "chercheurs": chercheurs,
                          "ita": ita,
                          "doctorants": doctorants,
                          "postdocs": postdocs,
                      }
                      )


def group(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]


def personnel(request):

    if request.method == 'GET':
        staff = Personnel.objects.all().filter(
            categorie="ITA").filter(presence=True).order_by('nom')
        doctorants = Personnel.objects.all().filter(
            categorie="Doctorant").filter(presence=True).order_by('nom')
        postdocs = Personnel.objects.all().filter(
            categorie="Post-doc").filter(presence=True).order_by('nom')
        chercheurs = Personnel.objects.all().filter(
            categorie="Chercheur").filter(presence=True).order_by('nom')
        q = len(staff) // 7
        return render(request, 'membres.html',
                      {"groupstaff": group(staff, 7),
                       "staff": staff,
                       "groupdoctorants": group(doctorants, 9),
                       "doctorants": doctorants,
                       "grouppostdocs": group(postdocs, 7),
                       "postdocs": postdocs,
                       "groupchercheurs": group(chercheurs, 9),
                       "chercheurs": chercheurs,

                       }
                      )

def trombi(request):

    if request.method == 'GET':
        staff = Personnel.objects.all().filter(
            categorie="ITA").filter(presence=True).order_by('nom')
        doctorants = Personnel.objects.all().filter(
            categorie="Doctorant").filter(presence=True).order_by('nom')
        postdocs = Personnel.objects.all().filter(
            categorie="Post-doc").filter(presence=True).order_by('nom')
        chercheurs = Personnel.objects.all().filter(
            categorie="Chercheur").filter(presence=True).order_by('nom')
        #ALL sans Avin et Pascal ITA
        all = Personnel.objects.all().filter(presence=True).    \
            exclude(personnel_id=70).   \
            exclude(personnel_id=69).   \
            order_by('nom')
        one = all[0:33]
        two = all[33:51]
        three = all[51:len(all)]
        return render(request, 'trombi.html',
                      {
                          "staff": staff,
                          "doctorants": doctorants,
                          "postdocs": postdocs,
                          "chercheurs": chercheurs,
                          "all": all,
                          "one": one,
                          "two": two,
                          "three": three,
                       }
                      )