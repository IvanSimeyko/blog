from models import Article, Comment
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.shortcuts import redirect
from forms import CommentForm
from django.contrib import messages


class ArticleListView(ListView):
    model = Article
    paginate_by = 7
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        article = self.get_object()
        context['comment'] = article.comment_set.all()
        coment_form = CommentForm
        context['form'] = coment_form
        return context


def add_like(request, pk):
    try:
        if pk in request.COOKIES:
            redirect('home')
        else:
            article = Article.objects.get(id=pk)
            article.article_likes += 1
            # to save the database
            article.save()
            response = redirect('home')
            response.set_cookie(pk, 'test')
            return response
    except ObjectDoesNotExist:
        # show 404 page
        raise Http404
    return redirect('home')


def add_comment(request, pk):
    if request.POST and ('pause' not in request.session):
        # make variable (instance class CommentForm)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_article = Article.objects.get(id=pk)
            form.save()
            messages.success(request, "Comment successfully added")
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('articles:article_detail', pk)