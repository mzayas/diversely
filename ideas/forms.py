from django import forms
from ideas.models import Idea


class IdeaForm(forms.ModelForm):
    idea = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Wild ideas welcome...'
        }
    ))

    class Meta:
        model = Idea
        fields = ('idea',)
