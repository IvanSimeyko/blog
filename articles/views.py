from models import Article
from django.views.generic.list import ListView


class ArticleListView(ListView):
    model = Article
    paginate_by = 7
    context_object_name = 'articles'
