from django import forms
from datetime import datetime

class CommentaryForm(forms.Form):

    commentarist = forms.CharField()
    text_commentary = forms.CharField()