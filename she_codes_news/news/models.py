from django.db import models
from django.contrib.auth import get_user_model

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # these variables are fields in the database (search 'Django Model Field Reference')
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    img_url = models.CharField(max_length=200, default='https://picsum.photos/600')

# add categories, authors