#!/bin/bash
echo "Установка Marzban Shortlinks..."

# Установка зависимостей
apt update && apt install -y python3-pip nginx
pip3 install -r requirements.txt

# Настройка .env
cp .env.example .env
nano .env

# Установка systemd сервиса
bash src/service.sh

echo "Установка завершена! Используйте cli.py для управления сервисом."
