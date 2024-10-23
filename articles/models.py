from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.CharField(max_length=500)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)

    def __str__(self):
        return self.titre
