from models import Article, Comment
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


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
        return context