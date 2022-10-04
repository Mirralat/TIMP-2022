sudo touch /etc/systemd/system/lock.service
echo "[Unit]
Description=My bot
After=multi-user.target
 
[Service]
Type=idle
ExecStart=/home/worker/Desktop/timp/timp python3 nocreate.py
Restart=always
 
[Install]
WantedBy=multi-user.target" >> lock.service
