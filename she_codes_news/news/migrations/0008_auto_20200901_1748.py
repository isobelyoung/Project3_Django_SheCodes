# Generated by Django 3.0.8 on 2020-09-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20200901_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='story_img',
            field=models.ImageField(blank=True, default='/media/images/default_story.jpg', null=True, upload_to='images/'),
        ),
    ]
