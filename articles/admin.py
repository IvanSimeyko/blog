from django.contrib import admin
from models import Article, Comment, Tag
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField


class ArticleInline(admin.StackedInline):
    model = Comment
    extra = 1


class ArticleAdmin(MarkdownModelAdmin):
    list_display = ['article_title', 'article_date']
    search_fields = ['article_title', 'article_date']
    inlines = [ArticleInline]
    list_filter = ['article_date']
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
#admin.site.register(Comment, CommentAdmin)