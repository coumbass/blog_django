from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from articles.forms import ArticleForm
from articles.models import Article

def home(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})
def useradmin(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.auteur = request.user  # Associe l'article à l'utilisateur connecté
            article.save()
            messages.success(request, 'Article créé avec succès')
            return redirect('useradmin')  # Redirigez vers la page souhaitée après la sauvegarde
    else:
        form = ArticleForm()

    articles = Article.objects.all()  # Récupère tous les articles pour affichage
    return render(request, 'useradmin.html', {'form': form, 'articles': articles})

def new_article(request):
    # Définissez ici votre logique pour créer un nouvel article
    return render(request, "new_article.html")

def modifier_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES , instance=article)
        if form.is_valid():
            form.save()
            return redirect('useradmin')  # Redirection vers la liste après modification
    return redirect('useradmin')

def supprimer_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('useradmin')  # Redirection après suppression

    return render(request, 'useradmin')