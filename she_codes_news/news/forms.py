from django import forms
from django.forms import ModelForm
from .models import *

art_categories = (
    "Digital",
    "Photography",
    "Painting"
)

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'story_img', 'category']
        labels = {
            'title': 'Review Heading',
            'pub_date': 'Publication Date',
            'content': 'Your Review',
            'story_img': 'Upload a photo!',
            'category': 'Restaurant/cafe name'
        }
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select a date',
            'type':'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(StoryForm, self).__init__(*args, **kwargs)
        self.fields['story_img'].required = False
    