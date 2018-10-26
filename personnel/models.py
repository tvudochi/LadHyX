# coding=utf-8
from django.db import models


class Bureau(models.Model):

    class Meta:
        verbose_name = 'Bureau'
        verbose_name_plural = 'Bureaux'

    bureau = models.CharField(primary_key=True, max_length=8)

    def __str__(self):
        return self.bureau


class Telephone(models.Model):

    class Meta:
        verbose_name = 'Téléphone'
        verbose_name_plural = 'Téléphones'

    telephone = models.CharField(primary_key=True, max_length=12)

    def __str__(self):

        return self.telephone


class Email(models.Model):

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Email"

    email = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.email


class Personnel(models.Model):

    class Meta:
        verbose_name = 'Personnel'
        verbose_name_plural = 'Personnels'

    CATEGORIE = (
        ('Chercheur', 'Chercheur'),
        ('Doctorant', 'Doctorant'),
        ('Post-doc', 'Post-doc'),
        ('ITA', 'ITA'),
        ('Stagiaire', 'Stagiaire'),
        ('PSC', 'PSC'),
        ('PRL', 'PRL'),
        ('Visiteur', 'Visiteur'),
        ('Anciens', 'Anciens'),
    )

    FONCTION = (

        ('Maître de conférences (CNAM)', 'Maître de conférences (CNAM)'),
        ('Ingénieur de recherche (EP/X)', 'Ingénieur de recherche (EP/X)'),
        ('Directeur de recherche (CNRS)', 'Directeur de recherche (CNRS)'),
        ('Professeur chargé de cours (EP/X)',
         'Professeur chargé de cours (EP/X)'),
        ('Chargé de recherche (CNRS)', 'Chargé de recherche (CNRS)'),
        ('Directeur de recherche (CNRS) - Directeur du LadHyX',
         'Directeur de recherche (CNRS) - Directeur du LadHyX'),
        ('Professeur (EP/X) - Président du Département de Mécanique',
         'Professeur (EP/X) - Président du Département de Mécanique'),
        ('Maître de conférences (EP/X)', 'Maître de conférences (EP/X)'),
        ('Ingénieur de recherche (CNRS)', 'Ingénieur de recherche (CNRS)'),
        ('Directeur de recherche émérite (CNRS)',
         'Directeur de recherche émérite (CNRS)'),
        ('Chargé de recherche (CNRS)', 'Chargé de recherche (CNRS)'),
        ('Maître de conférences (EP/X) - Directeur-adjoint du LadHyX',
         'Maître de conférences (EP/X) - Directeur-adjoint du LadHyX'),
        ('Enseignante-chercheuse (ENSTA)',
         'Enseignante-chercheuse (ENSTA)'),
        ('Chercheur associé (CNRS)', 'Chercheur associé (CNRS)'),
        ('Professeur associé (EP/X)', 'Professeur associé (EP/X)'),
        ('Doctorant', 'Doctorant'),
        ('Chercheur postdoctoral', 'Chercheur postdoctoral'),
        ('Ingénieur d\'études', 'Ingénieur d\'études'),
        ('Technicien mécanicien', 'Technicien mécanicien'),
        (
            'Secrétariat de direction, Missions',
            'Secrétariat de direction, Missions'),
        ('Administratrice, Ressource humaines',
         'Administratrice, Ressource humaines'),
        ('Gestionnaire, secrétaire', 'Gestionnaire, secrétaire'),
        ('Ingénieur systèmes', 'Ingénieur systèmes'),
    )

    personnel_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    categorie = models.CharField(max_length=100, choices=CATEGORIE, blank=True)
    fonction = models.CharField(max_length=100, blank=True)
    fonction1 = models.CharField(max_length=100, blank=True)
    fonction2 = models.CharField(max_length=100, blank=True)
    page_perso = models.CharField(max_length=500, blank=True)
    Photo = models.CharField(max_length=500, blank=True)
    tuteur = models.ManyToManyField('self', symmetrical=False, null=True,
                                    blank=True)
    bureau = models.ManyToManyField(Bureau, blank=True)
    telephone = models.ManyToManyField(Telephone, blank=True)
    email = models.ManyToManyField(Email, blank=True)
    debut_mail = models.CharField(max_length=500, blank=True, null=True)
    fin_mail = models.CharField(max_length=500, blank=True, null=True)
    presence = models.BooleanField(default=True)
    phdtopic = models.CharField(max_length=500, blank=True, null=True)
    extern_advisors = models.CharField(max_length=100, blank=True, null=True)
    lieu = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.nom, self.prenom)
