from django.contrib import admin
from models import About_me
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField


class About_meAdmin(MarkdownModelAdmin):
    search_fields = ['info']
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

admin.site.register(About_me, About_meAdmin)
