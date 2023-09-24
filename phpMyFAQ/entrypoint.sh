#!/bin/bash
echo "RewriteEngine On" > /var/www/html/.htaccess
echo "RewriteBase /" >> /var/www/html/.htaccess
# 他の.htaccessのルールを追加
exec "$@"
