from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Creates form to be displayed in :view:`blog.post_detail` using only
    the body field of the comment
    """
    class Meta:
        model = Comment
        fields = ('body',)