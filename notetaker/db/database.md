## Docker
### Create
```
docker volume create notes-db
```

### Link
```
docker run -dp 8000:8000 -v notes-db:/app/db dj
```