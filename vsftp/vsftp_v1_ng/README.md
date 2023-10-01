# vsftp
[Docker Image](https://hub.docker.com/r/fauria/vsftpd/)
## モード
* パッシブモード：FTPサーバからクライアントへのデータ接続を行わない。
* アクティブモード：FTPサーバからクライアントへのデータ接続を行う。

## FTPサーバの構築方法
### vsftpdのイメージ取得
```bash
docker pull fauria/vsftpd
```
### vsftpdのコンテナを起動する。（パッシブモード）
```bash
docker run -d \
  -e FTP_USER=myuser \
  -e FTP_PASS=mypassword \
  -p 21:21 \
  -p 21100-21110:21100-21110 \
  --name vsftpd_container \
  fauria/vsftpd

```
```pwershell
docker run -d `
  --rm `
  -e FTP_USER=myuser `
  -e FTP_PASS=mypassword `
  -p 21:21 `
  -p 1024-19221:1024-19221 `
  -v ${pwd}/data:/home/vsftpd `
  --name vsftpd_container `
  fauria/vsftpd
```
 -v /path/to/local/folder:/home/vsftpd `
 