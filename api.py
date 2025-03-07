import os
import requests
from dotenv import load_dotenv

load_dotenv()

MARZBAN_API_URL = os.getenv("MARZBAN_API_URL")
SUDO_USERNAME = os.getenv("SUDO_USERNAME")
SUDO_PASSWORD = os.getenv("SUDO_PASSWORD")

def get_token():
    """Получение токена API"""
    response = requests.post(f"{MARZBAN_API_URL}/admin/token", json={"username": SUDO_USERNAME, "password": SUDO_PASSWORD})
    return response.json().get("token")

def get_subscriptions():
    """Получение списка подписок"""
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{MARZBAN_API_URL}/admin/users", headers=headers)
    return response.json()

def update_subscription(subscription_id, short_link):
    """Обновление ссылки подписки в Marzban"""
    token = get_token()
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    data = {"subscription_link": short_link}
    requests.put(f"{MARZBAN_API_URL}/admin/users/{subscription_id}", json=data, headers=headers)
