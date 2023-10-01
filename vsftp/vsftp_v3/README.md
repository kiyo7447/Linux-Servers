#  
[リソース](https://github.com/epoweripione/docker-vsftpd-alpine/)

## 実行方法（docker-compose.ymlを使う）
```bash

docker-compose up -d
```
## 実行方法（docker runを使う）
```powershell
docker build -t vsftp-image .
docker run -d -p 20-21:20-21 -p 21100-21110:21100-21110 -e FTP_USER=myuser -e FTP_PASS=mypass -e PASV_ADDRESS=127.0.0.1 -v ${pwd}/ftp:/home/ftp -v ${pwd}/logs/vsftpd/:/var/log/vsftpd/ --name vsftpd --restart=always vsftp-image

```

## FTPユーザアカウントの追加
```bash
docker ps

docker exec -it 181ab6ae1fad sh

echo "admin:$(openssl passwd -1 admin)" >> /etc/vsftpd/virtual_users
cat > /etc/vsftpd/vsftpd_user_conf/admin <<EOF
anon_world_readable_only=NO
write_enable=YES
anon_upload_enable=YES
anon_mkdir_write_enable=YES
anon_other_write_enable=YES
local_root=/home/ftp/
EOF
```


## 同じエラーが発生してだめだった。
```bash
o$ ftp localhost
DrifterMiniPC に接続しました。
220 Welcome to FTP Server
200 Always in UTF8 mode.
ユーザー (DrifterMiniPC:(none)): admin
331 Please specify the password.
パスワード: 
230 Login successful.
ftp> ls
500 Bad EPRT protocol.
425 Use PORT or PASV first.
ftp> 
```
