from django.contrib import admin
from models import Article, Comment


class ArticleInline(admin.StackedInline):
    model = Comment
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article_title', 'article_date']
    search_fields = ['article_title', 'article_date']
    inlines = [ArticleInline]
    list_filter = ['article_date']

admin.site.register(Article, ArticleAdmin)
#admin.site.register(Comment, CommentAdmin)