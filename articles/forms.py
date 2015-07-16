from django import forms
from models import Comment
from django_markdown.widgets import MarkdownWidget


class CommentForm(forms.ModelForm):
    comment_text = forms.CharField( widget=MarkdownWidget() )

    class Meta:
        model = Comment
        fields = ('comment_text',)
