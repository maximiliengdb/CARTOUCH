# -*- coding: utf-8 -*-

from django import forms
from CARTOUCH.models import Cartouche, Fichier, Infos
from django.forms.widgets import Widget

class Formulaire_Ajout_Cartouche (forms.ModelForm):
    
        fichiers = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        labels = {
            'file_field' : (''),
            }
        class Meta:
            model = Cartouche
            fields = ['nom', 'description', 'auteur', 'matiere', 'type']
            widgets = {
            'nom' : forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'Un petit titre'}),
            'description' : forms.TextInput (attrs={'class': 'form-control', 'placeholder': "Une petite description"}),
            'auteur' : forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'Merci qui?'}),
        }
            
            labels ={
        'nom' : (''),
        'description' : (''),
        'auteur' : (''),
        }

            
class Formulaire_Ajout_Info (forms.ModelForm):
    
        
        class Meta:
            model = Infos
            fields = ['titre', 'auteur', 'info']
            widgets = {
            'titre' : forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'Un petit titre'}),
            'info' : forms.Textarea (attrs={'class': 'form-control', 'placeholder': "L'info"}),
            'auteur' : forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'Merci qui?'}),
        }
            
            labels ={
        'titre' : (''),
        'info' : (''),
        'auteur' : (''),
        }