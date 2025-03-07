#!/bin/bash
echo "[Unit]
Description=Marzban Shortlinks
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/marzban-shortlinks/src/main.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/marzban-shortlinks.service

systemctl enable marzban-shortlinks
systemctl start marzban-shortlinks
