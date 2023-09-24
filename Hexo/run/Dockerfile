# Node.jsのイメージを使用
FROM node:14

# 作業ディレクトリを設定
WORKDIR /app

# Hexo CLIをインストール
RUN npm install -g hexo-cli

# 依存パッケージをインストール
COPY package.json package-lock.json ./
RUN npm install

# プロジェクトファイルをコピー
COPY . .

# Hexoサーバーを起動するコマンドを指定
CMD ["hexo", "server"]
