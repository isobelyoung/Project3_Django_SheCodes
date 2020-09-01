from django import forms
from django.forms import ModelForm
from .models import *


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'story_img']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select a date',
            'type':'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(StoryForm, self).__init__(*args, **kwargs)
        self.fields['story_img'].required = False
    