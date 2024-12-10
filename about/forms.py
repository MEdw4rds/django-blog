from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    Creates form to be displayed in :view:`about.about_me`
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message',)