# nginx
## 概要
nginx SSLのサンプルです。
```powershell
docker-compose up -d
```
## ブラウザでアクセス
```powershell
https://localhost/
```
# エラー
## nginx.confは、UTF-8（BOM無し）、LFで保存してください。
下記のエラーが発生します。
```powershell
o$ docker-compose up  
[+] Running 2/0
 ✔ Network nginx_default    Created                                                 0.0s 
 ✔ Container nginx-nginx-1  Created                                                 0.0s 
Attaching to nginx-nginx-1
nginx-nginx-1  | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
nginx-nginx-1  | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
nginx-nginx-1  | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
nginx-nginx-1  | 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
nginx-nginx-1  | 10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
nginx-nginx-1  | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
nginx-nginx-1  | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
nginx-nginx-1  | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
nginx-nginx-1  | /docker-entrypoint.sh: Configuration complete; ready for start up       
nginx-nginx-1  | 2023/09/23 10:42:41 [emerg] 1#1: unknown directive "http" in /etc/nginxx/nginx.conf:1
nginx-nginx-1  | nginx: [emerg] unknown directive "http" in /etc/nginx/nginx.conf:1     
nginx-nginx-1 exited with code 1
o$ 
```
## https://localhost/ にアクセスすると、「保護されていない通信」という文字がブラウザに出ます。
これは、自己証明書を使っているからです。
