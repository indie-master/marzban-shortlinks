import os
import pymysql
import sqlite3
from dotenv import load_dotenv

load_dotenv()

DB_TYPE = os.getenv("DB_TYPE", "sqlite")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

def get_db_connection():
    """Подключение к БД"""
    if DB_TYPE == "mysql":
        return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    else:
        return sqlite3.connect("shortlinks.db")

def save_short_link(conn, subscription_id, short_link):
    """Сохранение короткой ссылки"""
    cursor = conn.cursor()
    cursor.execute("INSERT INTO links (subscription_id, short_link) VALUES (%s, %s) ON DUPLICATE KEY UPDATE short_link=%s",
                   (subscription_id, short_link, short_link))
    conn.commit()
