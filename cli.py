import argparse
import os

def start_service():
    os.system("systemctl start marzban-shortlinks")

def stop_service():
    os.system("systemctl stop marzban-shortlinks")

def restart_service():
    os.system("systemctl restart marzban-shortlinks")

def status_service():
    os.system("systemctl status marzban-shortlinks")

parser = argparse.ArgumentParser(description="Управление сервисом Marzban Shortlinks")
parser.add_argument("command", choices=["start", "stop", "restart", "status"], help="Команда")

args = parser.parse_args()

if args.command == "start":
    start_service()
elif args.command == "stop":
    stop_service()
elif args.command == "restart":
    restart_service()
elif args.command == "status":
    status_service()
