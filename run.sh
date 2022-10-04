#/bin/bash

python3 var.py
python3 secure.py
python3 nocreate.py
sudo touch /etc/systemd/system/lock.service
echo "[Unit]
Description=My bot
After=multi-user.target
 
[Service]
Type=idle
ExecStart=/usr/bin/python nocreate.py
Restart=always
 
[Install]
WantedBy=multi-user.target" >> lock.service