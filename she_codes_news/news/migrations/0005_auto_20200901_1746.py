# Generated by Django 3.0.8 on 2020-09-01 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200829_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='story_img',
            field=models.ImageField(blank=True, default='default_story.jpg', null=True, upload_to='images/'),
        ),
    ]
