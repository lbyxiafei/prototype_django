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