# Generated by Django 3.0.8 on 2020-08-22 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='img_url',
            field=models.CharField(default='https://picsum.photos/600', max_length=200),
        ),
    ]