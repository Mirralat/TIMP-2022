#/bin/bash

python3 var.py
python3 secure.py
python3 nocreate.py
sudo systemctl daemon-reload
sudo systemctl start lock.service
