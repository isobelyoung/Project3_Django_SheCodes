# Generated by Django 3.0.8 on 2020-08-29 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.TextField(blank=True, max_length=20),
        ),
    ]
