from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # these variables are fields in the database (search 'Django Model Field Reference')
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    img_url = models.CharField(max_length=200, default='https://picsum.photos/600')

# add categories, authors