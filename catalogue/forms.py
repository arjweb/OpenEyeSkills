from django import forms
from .models import CatalogueItem


class ContributeForm(forms.Form):
    title = forms.CharField(max_length=80, required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))
    what_learn = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder':'This is important, please be specific.'}), label='What will you learn')

    # fields = ['topic_area', 'title', 'description', 'link', 'what_learn', 'how_apply', 'level', 'relevant_to', 'discovered_by']
