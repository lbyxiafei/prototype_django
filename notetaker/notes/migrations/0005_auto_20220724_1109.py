# Generated by Django 3.2 on 2022-07-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_merge_0003_auto_20220718_1324_0003_auto_20220718_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag2post',
            name='post',
        ),
        migrations.RemoveField(
            model_name='tag2post',
            name='tag',
        ),
        migrations.RenameField(
            model_name='bookmark',
            old_name='bookmark',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='title',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='tag',
            field=models.ManyToManyField(to='notes.Tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='notes.Tag'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Tag2Bookmark',
        ),
        migrations.DeleteModel(
            name='Tag2Post',
        ),
    ]
