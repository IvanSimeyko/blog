# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from articles.models import Article, Category, Tag


#def home(request):
#   article_list = Article.objects.all()
    #tags_list = article_list.article_set.all()
#    return render(request, 'base.html', {'article_list': article_list})


def category(request, pk):
    # делаем выборку выбранной категории
    category = get_object_or_404(Category, id=pk)
    # выбираем все статьи по выбранной категории
    posts = category.article_set.published
    # возвращаем выбранную категорию и статьи в шаблон category.html
    return render(request, 'tagpage.html', {'posts': posts,
                                            'category': category})


def tag(request, pk):
    tag = get_object_or_404(Tag, id=pk)
    posts = tag.article_set.all()
    return render(request, 'tagpage.html', {'posts': posts,
                                            'tag': tag})

