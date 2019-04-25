```shell
docker ps --format "{{.ID}}: {{.Image}}"
docker ps -q | xargs docker inspect --format '{{.ID}}: {{.State.Pid}} {{.Name}}'
```