#
[リソース](https://github.com/fauria/docker-vsftpd/)

## この実行はうまく行かなかった
```bash
データポートは開けない。
・・
ユーザー (DrifterMiniPC:(none)): myuser
331 Please specify the password.
パスワード:
530 Login incorrect.
ログインできませんでした。
ftp> user
ユーザー名 admin
331 Please specify the password.
パスワード:
230 Login successful.
ftp> ls
500 Bad EPRT protocol.
425 Use PORT or PASV first.
ftp> dir
425 Use PORT or PASV first.
ftp> mkdir ok
257 "/ok" created
ftp> rmdir ok
250 Remove directory operation successful.
ftp> ls  
接続がリモート ホストによって閉じられました。
ftp> user     
接続されていません。
```
