# ファイル共有サーバー Nextcloud
## 概要
Nextcloudは、ファイル共有サーバーです。
## 実行方法
### 起動
```bash
$ docker-compose up -d
```
# phpMyFAQ
## 概要
phpMyFAQは、FAQ管理ツールです。
## 実行方法
### 起動
```powershell
$ docker-compose up -d
```
# エラー
## マウントしてみたが、ファイルが見えない
```yaml
version: '3'
services:
  phpmyfaq:
    image: phpmyfaq/phpmyfaq
    volumes:
      - ./.htaccess:/var/www/html/.htaccess # こちらがマウント設定
```
エラー
sed: couldn't edit .htaccess: not a regular file というエラーは、.htaccess ファイルに対する sed コマンドが失敗していることを意味します。このエラーが発生する理由としては以下のようなものが考えられます：  
.htaccess ファイルがコンテナ内で既に存在するが、通常のファイルではない（例えば、ディレクトリやシンボリックリンクなど）。  
.htaccess ファイルがマウントされているが、何らかの理由で通常のファイルとして認識されない。
```bash
x$ dc up
[+] Running 2/0
 ✔ Container phpmyfaq-phpmyfaq-1  Created                                                                                                                                                                0.0s 
 ✔ Container phpmyfaq-mysql-1     Running                                                                                                                                                                0.0s 
Attaching to phpmyfaq-mysql-1, phpmyfaq-phpmyfaq-1
phpmyfaq-phpmyfaq-1  | Module rewrite already enabled
phpmyfaq-phpmyfaq-1  | Module headers already enabled
phpmyfaq-phpmyfaq-1  | sed: couldn't edit .htaccess: not a regular file
phpmyfaq-phpmyfaq-1 exited with code 4
```
## Dockerfileを利用する
```yaml
version: '3'
services:
  phpmyfaq:
    build: ./path/to/Dockerfile/
    ports:
      - "8080:80"
```
```dockerfile
# Dockerfileの内容（例）
FROM phpmyfaq/phpmyfaq
COPY ./.htaccess /var/www/html/.htaccess
```
## entrypoint scriptを使用する
```yaml
version: '3'
services:
  phpmyfaq:
    image: phpmyfaq/phpmyfaq
    entrypoint: ["/path/to/entrypoint.sh"]
    ports:
      - "8080:80"
```
実行権限を与える
```bash
chmod +x entrypoint.sh
```
# TODO
## 動かすのを諦める。
