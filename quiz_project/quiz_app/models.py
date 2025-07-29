from django.db import models

class Formateur(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

class Quiz(models.Model):
    ETAT_CHOICES = [('dispo', 'Disponible'), ('non_dispo', 'Non disponible')]
    titre = models.CharField(max_length=10)
    nr_questions = models.IntegerField()
    etat = models.CharField(max_length=20, choices=ETAT_CHOICES, default='non_dispo')
    formateur = models.ForeignKey(Formateur, on_delete=models.CASCADE)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.nr_questions <= 0:
            raise ValidationError("Le nombre de questions doit être supérieur à zéro.")
        if len(self.titre) > 10:
            raise ValidationError("Le titre doit contenir au maximum 10 caractères.")

class Question(models.Model):
    text = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)