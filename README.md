![Docker](https://github.com/w84thesun/list-employees/workflows/Docker/badge.svg)

# list-employees

Чтобы запустить в docker:
```shell script
docker run \
    --name app \
    --rm \
    -e PORT=9090 \
    -e GRACEFUL_TIMEOUT=5 \
    -e MONGO_DB=test \
    -e MONGO_URI=mongodb://localhost:27017/test \
    -p 9090:9090 \
    docker.pkg.github.com/w84thesun/list-employees/list-employees-app:latest
```

Для получения данных доступно два метода: 
* `findByField` - фильтрация по полю
* `findByRange` - фильтрация по диапазону значений с включением граничных значений
