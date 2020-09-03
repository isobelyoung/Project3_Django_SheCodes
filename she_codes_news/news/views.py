from django.views import generic
from .models import NewsStory
from django.urls import reverse_lazy
# from .forms import StoryForm

from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *

from users.models import CustomUser

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by('-pub_date').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date').all()[:4] #  added order_by to sort stories by date
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date') #  added order_by to sort stories by date
        # context['by_author'] = NewsStory.objects.all().filter('author', flat=True)
        return context

    @property
    def get_auth(self, id):
        return NewsStory.objects.all().filter(author=id)

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'


class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CategoryView(generic.ListView):
    template_name="news/storiesByCategory.html"
    model = NewsStory
    context_object_name = "story"

    def __init__(self):
        self.category = NewsStory.category

    def get_queryset(self):
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_categories'] = NewsStory.objects.all().order_by('-pub_date')
        
        context['Digital'] = NewsStory.objects.order_by('-pub_date').filter(category__contains='Digital')
        context['Digital_sneak_peek'] = NewsStory.objects.order_by('-pub_date').filter(category__contains='Digital')[:4]
        context['Photography'] = NewsStory.objects.order_by('-pub_date').filter(category__contains='Photography')
        context['Photography_sneak_peek'] = NewsStory.objects.order_by('-pub_date').filter(category__contains='Photography')[:4]
        context['Painting'] = NewsStory.objects.order_by('-pub_date').filter(category__contains='Painting')
        context['Painting_sneak_peek'] = NewsStory.objects.order_by('-pub_date').filter(category__contains='Painting')[:4]
        
        return context

class DigitalView(generic.ListView):
    template_name="news/categoryDigital.html"
    model = NewsStory
    context_object_name = "story"

    def __init__(self):
        self.category = NewsStory.category

    def get_queryset(self):
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_categories'] = NewsStory.objects.all().order_by('-pub_date')
        
        context['Digital'] = NewsStory.objects.order_by('-pub_date').filter(category__contains='Digital')
        context['Digital_sneak_peek'] = NewsStory.objects.order_by('-pub_date').filter(category__contains='Digital')[:4]
        
        return context

class PhotographyView(generic.ListView):
    template_name="news/categoryPhotography.html"
    model = NewsStory
    context_object_name = "story"

    def __init__(self):
        self.category = NewsStory.category

    def get_queryset(self):
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_categories'] = NewsStory.objects.all().order_by('-pub_date')
        
        context['Photography'] = NewsStory.objects.order_by('-pub_date').filter(category__contains='Photography')
        context['Photography_sneak_peek'] = NewsStory.objects.order_by('-pub_date').filter(category__contains='Photography')[:4]
        
        return context

class PaintingView(generic.ListView):
    template_name="news/categoryPainting.html"
    model = NewsStory
    context_object_name = "story"

    def __init__(self):
        self.category = NewsStory.category

    def get_queryset(self):
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_categories'] = NewsStory.objects.all().order_by('-pub_date')
        
        context['Painting'] = NewsStory.objects.order_by('-pub_date').filter(category__contains='Painting')
        context['Painting_sneak_peek'] = NewsStory.objects.order_by('-pub_date').filter(category__contains='Painting')[:4]
        
        return context