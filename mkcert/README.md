# mkcert
## 概要
mkcertを使ってローカルで証明書を発行するためのコンテナイメージ
```powershell
#このイメージはないので、自分でビルドする必要がある
#x docker pull filipre/mkcert

docker build -t mkcert-image .

# コンテナを実行して証明書を生成します。以下のコマンドは、カレントディレクトリにmy-cert.pemとmy-key.pemという名前で証明書と鍵を生成します。
#x docker run --rm -v ${PWD}:/output filipre/mkcert -cert-file /output/my-cert.pem -key-file /output/my-key.pem example.com "*.example.com"

docker run --rm -v ${PWD}:/output mkcert-image -cert-file /output/my-cert.pem -key-file /output/my-key.pem example.com "*.example.com"
```
