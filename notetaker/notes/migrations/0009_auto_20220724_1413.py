# Generated by Django 3.2 on 2022-07-24 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_auto_20220724_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='bookmark',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='tag',
            field=models.ManyToManyField(to='notes.Tag'),
        ),
    ]
