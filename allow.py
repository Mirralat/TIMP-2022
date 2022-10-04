import subprocess
import os
from var import passwd, pwd

print('Try to guess a password!')
guess = input()


if guess == passwd:
    subprocess.run('sudo systemctl stop lock.service', shell=True, check=True)
    subprocess.run(f'sudo chattr -i {pwd}/template.tbl', shell=True, check=True)
    subprocess.run('sudo chmod 777 template.tbl', shell=True, check=True)

    names = []
    ls = subprocess.Popen(["ls", "-p", "."],  stdout=subprocess.PIPE,)
    grep = subprocess.Popen(["grep", "-v", "/$"],  stdin=ls.stdout, stdout=subprocess.PIPE,)
    files = grep.stdout

    for line in files:
        line = str(line, 'utf-8')
        line = line.replace("\n", '')  
        names.append(line)
    
    table = open("template.tbl", "r")
    tables = []

    for i in table:
        j = str(i)
        j = j.replace("\n", '')
        tables.append(j)
        

    for line in tables:
        if line in names:
            subprocess.run(f'sudo chattr -i {pwd}/{line}', shell=True, check=True)
            subprocess.run(f'sudo chmod 777 {pwd}/{line}', shell=True, check=True)
    print("Congrats! You guessed a password!")

else:
    print("Try again!")