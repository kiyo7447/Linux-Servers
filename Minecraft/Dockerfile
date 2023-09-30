# ベースイメージとしてUbuntuを使用
FROM ubuntu:latest

# Minecraftサーバーのバージョン
ARG MINECRAFT_VERSION=1.17.1

# 必要なパッケージをインストール
RUN apt-get update -y && \
    apt-get install -y wget openjdk-17-jre-headless

# Java JDKをインストール
# run apt install openjdk-17-jdk

# サーバーファイルをダウンロード
#RUN wget https://launcher.mojang.com/v1/objects/0a269b5f2c5b93b1712d0f5dc43b6182b9ab254e/server.jar -O minecraft_server.jar
#  https://www.minecraft.net/en-us/download/server
RUN wget https://piston-data.mojang.com/v1/objects/5b868151bd02b41319f54c8d4061b8cae84e665c/server.jar -O minecraft_server.jar

# サーバー設定ファイルをコピー（このファイルは事前に作成しておく）
COPY server.properties .

# EULAに同意
RUN echo "eula=true" > eula.txt

# サーバー起動コマンド
CMD ["java", "-Xmx1024M", "-Xms1024M", "-jar", "minecraft_server.jar", "nogui"]
