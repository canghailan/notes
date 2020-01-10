查找Inode占用最多文件
```shell
cd /var/lib/docker/aufs/diff
find . -xdev -type f | cut -d "/" -f 2 | sort | uniq -c | sort -n
```


Docker 清理
```shell
docker system prune -a --volumes
```

```
/var/lib/docker/image/aufs/distribution/v2metadata-by-diffid/sha256
```


申请新IP地址
```shell
dhclient
```

删除IP地址
```shell
ip addr del 1.1.1.1/24 dev eth0
```

删除密码
```shell
passwd -d root
```