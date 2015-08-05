from django import template
from articles.models import Article, Tag, Category, Comment

register = template.Library()

@register.inclusion_tag("right_sidebar.html")
def show_sidebar():
    tags = Tag.objects.all().order_by('name')
    categories = Category.objects.all().order_by("name")
    popular_articles = Article.objects.published().order_by('-article_likes')[:5]
    last_comment = Comment.objects.all().order_by('comment_date')[:5]
    return {'tags': tags, 'categories': categories, 'popular_articles': popular_articles, 'last_comment': last_comment}

