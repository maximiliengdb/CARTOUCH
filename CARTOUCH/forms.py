# -*- coding: utf-8 -*-

from django import forms
from CARTOUCH.models import Cartouche, Fichier, Infos
from django.forms.widgets import Widget

class Formulaire_Ajout_Cartouche (forms.ModelForm):
    
        file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        
        class Meta:
            model = Cartouche
            fields = ['nom', 'description', 'matiere', 'auteur', 'type']
            widgets = {
            'nom' : forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'Titre'}),
            'description' : forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'Description'}),

            'auteur' : forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'Auteur'}),
        }
            
class Formulaire_Ajout_Info (forms.ModelForm):
    
        
        class Meta:
            model = Infos
            fields = ['titre', 'info', 'auteur']
            widgets = {
            'titre' : forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'Titre'}),
            'info' : forms.TextInput (attrs={'class': 'form-control', 'placeholder': "L'info"}),
            'auteur' : forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'Auteur'}),
        }