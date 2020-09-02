from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q

art_categories = (
    "Digital",
    "Photography",
    "Painting"
)

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="stories",
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    story_img = models.ImageField(upload_to='images/', null=True, blank=True, default='/media/images/default_story.jpg') # add default image!
    category = models.CharField(max_length=200, default="All cafes")


    # objects = PostManager()

# class StoryManager(models.Manager):
#     def search(self, query=None):
#         qs = self.get_queryset()
#         if query is not None:
#             or_lookup = (Q(title__icontains=query) | 
#                          Q(description__icontains=query)|
#                          Q(slug__icontains=query)
#                         )
#             qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
#         return qs
