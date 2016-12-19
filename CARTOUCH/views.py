# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from CARTOUCH.forms import *
from CARTOUCH.models import *
from _datetime import date


def mdp (request):
    
    if request.method == 'POST':  
        
        token = request.POST['token']
        
        if token == 'carnage':
            
            request.session['acces'] = True
            return redirect(home)
    
    return render(request, 'CARTOUCH/mdp.html', locals())

def test (request):
    
    test = False
    
    try : 
        if request.session['acces'] == True :
            test = True
    
    except :
        pass
    
    return test


def home(request):

    if test(request) == False :
        return redirect(mdp)
    
    try :
        cartouches = Cartouche.objects.all()[5:]
        infos = Infos.objects.all()[2:]
    except : 
        pass
    
    return render(request, 'CARTOUCH/index.html', locals()) 

def ajout_cartouche(request):
    
    if test(request) == False :
        return redirect(mdp)

    
    if request.method == 'POST':  
        form = Formulaire_Ajout_Cartouche(request.POST, request.FILES)  
        
        if form.is_valid():
            
            cartouche = Cartouche
            fichier = Fichier
             
            nom = form.cleaned_data['nom']
            description = form.cleaned_data['description']
            auteur = form.cleaned_data['auteur']
            matiere = form.cleaned_data['matiere']
            type = form.cleaned_data['type']

            fichiers = request.FILES.getlist('file_field')
            
            cartouche = Cartouche(nom = nom, description = description, auteur = auteur, matiere = matiere, type = type)
            cartouche.save()
            
            
            for f in fichiers:
                fichier = Fichier(upload=f, cartouche = cartouche)
                fichier.save()
                
    else: 
        form = Formulaire_Ajout_Cartouche()  
    

    return render(request, 'CARTOUCH/ajout.html', locals())


def ajout_info(request):
    
    if test(request) == False :
        return redirect(mdp)

    
    if request.method == 'POST':  
        form = Formulaire_Ajout_Info(request.POST)  
        
        if form.is_valid():
            
            info = Infos
             
            titre = form.cleaned_data['titre']
            info = form.cleaned_data['info']
            auteur = form.cleaned_data['auteur']
            
            
            info = Infos(titre = titre, info = info, auteur = auteur)
            info.save()
            
         
                
    else: 
        form = Formulaire_Ajout_Info()  
    

    return render(request, 'CARTOUCH/ajoutinfo.html', locals())

def document(request, ref):
    
    if test(request) == False :
        return redirect(mdp)

    ref = request.GET['ref']
    
    cartouche = Cartouche.objects.get(id = ref)
    documents = Fichier.objects.filter(cartouche = cartouche)
    

    return render(request, 'CARTOUCH/consultation.html', locals())

def lesdocuments(request, matiere):
    
    if test(request) == False :
        return redirect(mdp)
    
    matiere = request.GET['matiere']

    cartouches = Cartouche.objects.filter(matiere = matiere)
    cartouches_cours = Cartouche.objects.filter(matiere = matiere, type = "Cours")
    cartouches_exo = Cartouche.objects.filter(matiere = matiere, type = "EXO")
    cartouches_annale = Cartouche.objects.filter(matiere = matiere, type = "Annales")
    
    return render(request, 'CARTOUCH/LesDocuments.html', locals())

def lesmatieres(request):
    
    if test(request) == False :
        return redirect(mdp)

    return render(request, 'CARTOUCH/LesMatieres.html', locals())