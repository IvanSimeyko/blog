# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from articles.models import Article, Category, Tag


def home(request):
    articles = Article.objects.all()

    return render(request, 'base.html', {'articles': articles})


def category(request, pk):
    # делаем выборку выбранной категории
    category = get_object_or_404(Category, id=pk)
    # выбираем все статьи по выбранной категории
    posts = category.article_set.all()
    # возвращаем выбранную категорию и статьи в шаблон category.html
    return render(request, 'tagpage.html', {'posts': posts,
                                            'category': category})


def tag(request, pk):
    category = get_object_or_404(Tag, id=pk)
    posts = category.article_set.all()
    return render(request, 'tagpage.html', {'posts': posts,
                                            'category': category})

