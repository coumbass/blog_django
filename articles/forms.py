from django import forms
from .models import Article



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article # Le modèle associé au formulaire
        fields = ['titre','resume','contenu','image'] # Les champs à afficher dans le formulaire