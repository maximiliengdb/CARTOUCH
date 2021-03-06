# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-20 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartouche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=60)),
                ('auteur', models.CharField(max_length=60)),
                ('type', models.CharField(choices=[('Cours', 'Cours'), ('EXO', 'Exercices'), ('Annales', 'Annales')], max_length=45)),
                ('matiere', models.CharField(choices=[('Contrôle de gestion en milieu spécifique', 'Contrôle de gestion en milieu spécifique'), ("Le système d'information en contrôle de gestion", "Le système d'information en contrôle de gestion"), ('Droit du financement des entreprises', 'Droit du financement des entreprises'), ('Normalisation et normes comptables internationales', 'Normalisation et normes comptables internationales'), ("Pilotage de l'entreprise et maîtrise des risques", "Pilotage de l'entreprise et maîtrise des risques"), ('Individus et organisations : pouvoir, culture et prise de décision', 'Individus et organisations : pouvoir, culture et prise de décision'), ('Glob’strat', 'Glob’strat'), ("Le monde des affaires dans l'art", "Le monde des affaires dans l'art"), ("Responsabilité dans l'entreprise et développement durable", "Responsabilité dans l'entreprise et développement durable")], max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Fichier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='document/')),
                ('cartouche', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CARTOUCH.Cartouche')),
            ],
        ),
        migrations.CreateModel(
            name='Infos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=30)),
                ('info', models.CharField(max_length=350)),
                ('auteur', models.CharField(max_length=60)),
            ],
        ),
    ]
