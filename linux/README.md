查找Inode占用最多文件
```shell
cd /var/lib/docker/aufs
find . -xdev -type f | cut -d "/" -f 2 | sort | uniq -c | sort -n
```


Docker 清理
```shell
docker system prune -a --volumes
```

```
/var/lib/docker/image/aufs/distribution/v2metadata-by-diffid/sha256
```