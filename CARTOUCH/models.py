# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

MATIERES = (
    ('Contrôle de gestion en milieu spécifique', 'Contrôle de gestion en milieu spécifique'),
    ("Le système d'information en contrôle de gestion", "Le système d'information en contrôle de gestion"),
    ("Droit du financement des entreprises", "Droit du financement des entreprises"),
    ("Normalisation et normes comptables internationales", "Normalisation et normes comptables internationales"),
    ("Pilotage de l'entreprise et maîtrise des risques", "Pilotage de l'entreprise et maîtrise des risques"),
    ("Individus et organisations : pouvoir, culture et prise de décision", "Individus et organisations : pouvoir, culture et prise de décision"),
    ("Glob’strat", "Glob’strat"),
    ("Le monde des affaires dans l'art", "Le monde des affaires dans l'art"),
    ("Responsabilité dans l'entreprise et développement durable", "Responsabilité dans l'entreprise et développement durable"),
   
)

TYPES = (
    ('Cours', 'Cours'),
    ('EXO', "Exercices"),
    ('Annales', "Annales"),
)

class Infos(models.Model):
    
    titre = models.CharField(max_length=30)
    info = models.CharField(max_length=350)
    auteur = models.CharField(max_length=60)
    

class Cartouche(models.Model):
    
    nom = models.CharField(max_length=30)
    date_fichier = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=60)
    auteur = models.CharField(max_length=60)
    type = models.CharField(
        max_length=45,
        choices = TYPES )
    matiere = models.CharField(
        max_length=120,
        choices = MATIERES )

class Fichier(models.Model):
    
    cartouche = models.ForeignKey(Cartouche)
    upload = models.FileField(upload_to="document/")
    