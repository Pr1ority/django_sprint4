# Generated by Django 3.2.16 on 2024-04-16 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_comments_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments_count',
        ),
    ]
