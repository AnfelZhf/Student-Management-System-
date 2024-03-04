from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from .models import Etudiant
from django.http import HttpResponseRedirect



# Create your views here.








def ajouter_etudiant(request):
    message = None
    
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        matricule = request.POST.get('matricule')

        # Vérification si tous les champs sont remplis
        if not (nom and prenom and matricule):
            message = 'Veuillez remplir tous les champs.'
        else:
            # Vérification si un étudiant avec le même matricule existe déjà
            if Etudiant.objects.filter(matricule=matricule).exists():
                # Étudiant avec le même matricule existe déjà
                message = 'Un étudiant avec ce matricule existe déjà.'
            else:
                # Création de l'étudiant seulement si tous les champs sont remplis
                Etudiant.objects.create(nom=nom, prenom=prenom, matricule=matricule)
                return redirect('liste_etudiants')
    
    return render(request, 'ajouter_etudiant.html', {'message': message})

def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'liste_etudiants.html', {'etudiants': etudiants})
 


def accueil(request):
    return render(request, 'accueil.html')

def vider_liste_etudiants(request):
    Etudiant.objects.all().delete()
    return redirect('liste_etudiants')


# views.py

def modifier(request):
    mem=Etudiant.objects.all()
    return render(request,'modifier.html',{'mem':mem})



def update(request,id):
    mem=Etudiant.objects.get(id=id)
    return render(request,'modifier_e.html',{'mem':mem})

def supprimer(request):
    mem=Etudiant.objects.all()
    return render(request,'supprimer.html',{'mem':mem})

def delete(request,id):
    mem=Etudiant.objects.get(id=id)
    mem.delete()
    return redirect('liste_etudiants')


def modify(request,id):
    x=request.POST['nom']
    y=request.POST['prenom']
    z=request.POST['matricule']
    mem=Etudiant.objects.get(id=id)
    mem.nom=x
    mem.prenom=y
    mem.matricule=z
    mem.save()
    return redirect('liste_etudiants')














