# Conda/Python environment

`conda create --name dj python=3.7.5 django`
`conda activate dj`

# Django Crash Course Commands
`Kudos to Brad@TraversyMedia`

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

>>>  from notes.models import Bookmark, Post, Tag
>>>  from django.utils import timezone

>>>  bookmark1 = Bookmark(bookmark="Bookmark1", url="www.google.com", pub_date=timezone.now())
>>>  bookmark1.save()
>>>  post1 = Post(post="post1", content="hello world", pub_date=timezone.now())
>>>  post1.save()
>>>  tag1 = Tag(tag="tag1", pub_date=timezone.now())
>>>  tag1.save()
```

```bash
# Create admin user
python manage.py createsuperuser
```

```bash
# Create pages app
python manage.py startapp pages
```

# Docker

## Package preparation
- `pip list --format=freeze > requirements.txt`

## Create Dockerfile
```yml
FROM python:3.7

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
```

## Docker CMD
- `docker image build --name django -t 880413/python-django .`
- `docker run -publish 8000:8000 880413/python-django --name django`
- `docker push 880413/python-django`

- `docker build --tag python-django .`
- `docker run --publish 8000:8000 python-django`

## Docker Updates

## Docker Document
> [Overview](https://docs.docker.com/get-started/overview/)