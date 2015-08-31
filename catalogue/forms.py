from django import forms
from .models import CatalogueItem, JobType


class ContributeForm(forms.ModelForm):

    class Meta:
        model = CatalogueItem
        fields = ['title', 'topic_area', 'description', 'link', 'what_learn', 'how_apply', 'level', 'relevant_to', 'discovered_by']

    ROLE_CHOICES = [[x.id, x.job] for x in JobType.objects.all()]

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'To sell this resource to others'}), max_length=80, required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Clear, e.g. format, duration, activities...'}))
    link = forms.CharField(widget=forms.URLInput(attrs={'placeholder': 'If required, link to resource http://...'}), required=False)
    what_learn = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder':"This is important, it's the reason for adding this learning resource, so please be specific."}), label='What will you learn?')
    how_apply = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder':"How could this be put into action afterwards?"}), label='How could you apply this?')
    relevant_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=ROLE_CHOICES)

