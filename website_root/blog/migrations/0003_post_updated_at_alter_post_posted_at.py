# Generated by Django 4.2.6 on 2023-10-27 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
