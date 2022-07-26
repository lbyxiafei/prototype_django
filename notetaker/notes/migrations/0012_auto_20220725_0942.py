# Generated by Django 3.2 on 2022-07-25 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0011_auto_20220725_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='bookmark',
            field=models.ManyToManyField(to='notes.Bookmark'),
        ),
    ]