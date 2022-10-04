import os
import time
import shutil

with open('/home/worker/Documents/NameData/log.txt', 'r') as f:

    for i in f:
        count = i

    count = int(count)
    if count > 5:
        print('Sorry, you need to buy full version of program...')
        print('Input y or n!')
        answer = input()

        if answer == 'y':
            print('Price is 1 BTC!')
            exit(0)
        
        if answer == 'n':
            print('Uninstalling...')
            time.sleep(5)
            pwd = os.getcwd()
            shutil.rmtree(pwd)
            exit(0)

        else:
            print('Incorrect input...')
    else:
        count += 1
        to_wrie = str(count)
        with open('/home/worker/Documents/NameData/log.txt', 'w') as f:
            f.write(to_wrie)


print('Hello! Whats your name?')

name = input()

names = []


with open('/home/worker/Documents/NameData/naming.txt', 'r') as f:
    for i in f:
        i = i.replace('\n', '')
        names.append(i)

if name in names:
    print(f'Hello, my dear {name}, glad to see You again...')

else:
    f = open('/home/worker/Documents/NameData/naming.txt', 'a')
    f.write(name + '\n') 
    print(f'Hi, {name}! My name is program!')
