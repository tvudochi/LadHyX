# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bureau',
            fields=[
                ('bureau', models.CharField(max_length=8, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Bureau',
                'verbose_name_plural': 'Bureaux',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Email',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('personnel_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('categorie', models.CharField(blank=True, max_length=100, choices=[('Chercheur', 'Chercheur'), ('Doctorant', 'Doctorant'), ('Post-doc', 'Post-doc'), ('ITA', 'ITA'), ('Stagiaire', 'Stagiaire'), ('PSC', 'PSC'), ('PRL', 'PRL'), ('Visiteur', 'Visiteur'), ('Anciens', 'Anciens')])),
                ('fonction', models.CharField(blank=True, max_length=100, choices=[('Maître de conférences (CNAM)', 'Maître de conférences (CNAM)'), ('Ingénieur de recherche (EP/X)', 'Ingénieur de recherche (EP/X)'), ('Directeur de recherche (CNRS)', 'Directeur de recherche (CNRS)'), ('Professeur chargé de cours (EP/X)', 'Professeur chargé de cours (EP/X)'), ('Chargé de recherche (CNRS)', 'Chargé de recherche (CNRS)'), ('Directeur de recherche (CNRS) - Directeur du LadHyX', 'Directeur de recherche (CNRS) - Directeur du LadHyX'), ('Professeur (EP/X) - Président du Département de Mécanique', 'Professeur (EP/X) - Président du Département de Mécanique'), ('Maître de conférences (EP/X)', 'Maître de conférences (EP/X)'), ('Ingénieur de recherche (CNRS)', 'Ingénieur de recherche (CNRS)'), ('Directeur de recherche émérite (CNRS)', 'Directeur de recherche émérite (CNRS)'), ('Chargé de recherche (CNRS)', 'Chargé de recherche (CNRS)'), ('Maître de conférences (EP/X) - Directeur-adjoint du LadHyX', 'Maître de conférences (EP/X) - Directeur-adjoint du LadHyX'), ('Enseignante-chercheuse (ENSTA)', 'Enseignante-chercheuse (ENSTA)'), ('Chercheur associé (CNRS)', 'Chercheur associé (CNRS)'), ('Professeur associé (EP/X)', 'Professeur associé (EP/X)'), ('Doctorant', 'Doctorant'), ('Chercheur postdoctoral', 'Chercheur postdoctoral'), ("Ingénieur d'études", "Ingénieur d'études"), ('Technicien mécanicien', 'Technicien mécanicien'), ('Secrétariat de direction, Missions', 'Secrétariat de direction, Missions'), ('Administratrice, Ressource humaines', 'Administratrice, Ressource humaines'), ('Gestionnaire, secrétaire', 'Gestionnaire, secrétaire'), ('Ingénieur systèmes', 'Ingénieur systèmes')])),
                ('page_perso', models.CharField(blank=True, max_length=500)),
                ('Photo', models.CharField(blank=True, max_length=500)),
                ('bureau', models.ManyToManyField(blank=True, to='personnel.Bureau')),
                ('email', models.ManyToManyField(blank=True, to='personnel.Email')),
            ],
            options={
                'verbose_name': 'Personnel',
                'verbose_name_plural': 'Personnels',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('telephone', models.CharField(max_length=12, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Téléphone',
                'verbose_name_plural': 'Téléphones',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='personnel',
            name='telephone',
            field=models.ManyToManyField(blank=True, to='personnel.Telephone'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personnel',
            name='tuteur',
            field=models.ManyToManyField(blank=True, null=True, to='personnel.Personnel'),
            preserve_default=True,
        ),
    ]
