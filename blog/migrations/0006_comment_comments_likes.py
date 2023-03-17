# Generated by Django 4.1.7 on 2023-03-10 07:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_post_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comments_likes',
            field=models.ManyToManyField(related_name='comments_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
