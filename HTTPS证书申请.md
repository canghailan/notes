# HTTPS 证书申请

## 安装Certbot
```shell
```

## 申请证书
```shell
certbot certonly --preferred-challenges dns --server https://acme-v02.api.letsencrypt.org/directory --agree-tos --manual -d "*.whohow.cc"
```