from django.db import models



class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    matricule = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
