# Conda/Python environment

`conda create --name dj python=3.7.5 django`
`conda activate dj`

# Django Crash Course Commands
`Kudos to Brad@TraversyMedia`

```bash
# Install pipenv
pip install pipenv
```
```bash
# Create Venv
pipenv shell
```
```bash
# Install Django
pipenv install django
```
```bash
# Create project
django-admin startproject notetaker 
cd notetaker 
```
```bash
# Run server on http: 127.0.0.1:8000 (ctrl+c to stop)
python manage.py runserver
```
```bash
# Run initial migrations
python manage.py migrate
```
```bash
# Create notes app
python manage.py startapp notes 
```
```bash
# Create notes migrations
python manage.py makemigrations notes 
```
```bash
# Run migrations
python manage.py migrate
```
```bash
# Using the shell
python manage.py shell

>>>  from notes.models import Bookmark, Post, Tag, Tag2Bookmark, Tag2Post 
>>>  from django.utils import timezone

>>>  bookmark1 = Bookmark(bookmark="Bookmark1", url="www.google.com", pub_date=timezone.now())
>>>  bookmark1.save()
>>>  post1 = Post(post="post1", content="hello world", pub_date=timezone.now())
>>>  post1.save()
>>>  tag1 = Tag(tag="tag1", pub_date=timezone.now())
>>>  tag1.save()

>>>  t2b = Tag2Bookmark(tag=tag1, bookmark=bookmark1, pub_date=timezone.now())
>>>  t2b.save()
>>>  t2p = Tag2Post(tag=tag1, post=post1, is_linked=False, pub_date=timezone.now())
>>>  t2p.save()

>>>  Bookmark.objects.filter(id=1)
>>>  Bookmark.objects.get(pk=1)

>>>  t = Tag.objects.get(pk=2)
>>>  t.tag2bookmark_set.all()
>>>  p = Post.objects.get(pk=2)
>>>  p.tag2post_set.all()
>>>  tag2=Tag(tag='test',pub_date=timezone.now())
>>>  tag2.save()
>>>  p.tag2post_set.create(tag=tag2,is_linked=False,pub_date=timezone.now())
>>>  quit()
```
```bash
# Create admin user
python manage.py createsuperuser
```
```bash
# Create pages app
python manage.py startapp pages
```