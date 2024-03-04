from django.urls import path
from .views import ajouter_etudiant, liste_etudiants,accueil,vider_liste_etudiants,modifier,modify,update,supprimer,delete

urlpatterns = [
   
    
    path('', accueil, name='accueil'),
     
    path('ajouter/', ajouter_etudiant, name='ajouter_etudiant'),
    path('liste/', liste_etudiants, name='liste_etudiants'),
    path('vider-liste/', vider_liste_etudiants, name='vider_liste_etudiants'),
    path('modifier',modifier,name="modifier"),
    path('update/<int:id>/',update,name="update"),
    path('update/modify/<int:id>/',modify,name="modify"),
    path('supprimer',supprimer,name="supprimer"),
    path('delete/<int:id>/',delete,name="delete")


   


]
