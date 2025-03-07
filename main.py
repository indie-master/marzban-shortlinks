import os
from dotenv import load_dotenv
from api import get_subscriptions, update_subscription
from db import get_db_connection, save_short_link

# Загружаем переменные из .env
load_dotenv()
SUBDOMAIN = os.getenv("SUBDOMAIN")

def generate_short_link(subscription_id):
    """Генерация короткой ссылки"""
    return f"https://{SUBDOMAIN}/{subscription_id}"

def process_subscriptions():
    """Обрабатывает подписки, создавая короткие ссылки"""
    conn = get_db_connection()
    users = get_subscriptions()
    
    for user in users:
        short_link = generate_short_link(user['id'])
        save_short_link(conn, user['id'], short_link)
        update_subscription(user['id'], short_link)

if __name__ == "__main__":
    process_subscriptions()
