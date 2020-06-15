# list-employees

Чтобы запустить в docker:
```shell script
docker run \
    --name app \
    --rm \
    -e PORT=9090 \
    -p 9090:9090 \
    docker.pkg.github.com/w84thesun/list-employees/list-employees-app:latest
```