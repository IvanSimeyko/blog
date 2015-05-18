from django.shortcuts import render
from articles.models import Article, Comment


def home(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

