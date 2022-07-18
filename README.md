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

>>>  from notes.models import Bookmark, Post 
>>>  from django.utils import timezone
>>>  Bookmark.objects.all()
>>>  q = Bookmark(name="Bookmark1", tag="test", url="www.google.com" pub_date=timezone.now())
>>>  q.save()
>>>  q.id
>>>  q.name
>>>  Bookmark.objects.all()
>>>  Bookmark.objects.filter(id=1)
>>>  Bookmark.objects.get(pk=1)
>>>  q = Bookmark.objects.get(pk=1)

>>>  q.choice_set.all()
>>>  q.choice_set.create(choice_text='Django', votes=0)
>>>  q.choice_set.create(choice_text='Flask', votes=0)
>>>  q.choice_set.create(choice_text='Flask', votes=0)
>>>  q.choice_set.all()
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