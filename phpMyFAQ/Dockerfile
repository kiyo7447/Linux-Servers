# Dockerfileの内容（例）
FROM phpmyfaq/phpmyfaq
COPY ./.htaccess /var/www/html/.htaccess
# 権限を 776 に設定
RUN chmod 776 /var/www/html/.htaccess

ENV PMF_DB_HOST=mysql:3306 \
PMF_DB_USER=phpmyfaq \
PMF_DB_PASS=my-secret-pw

EXPOSE 80

# 失敗した。なぜか、ディレクトリができる。
# COPY ./entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh
# ENTRYPOINT ["/entrypoint.sh"]
# RUN chmod 776 /var/www/html/.htaccess
