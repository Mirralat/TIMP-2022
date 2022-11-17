import os
import os.path


def start_the_installation(file, filename, data):
    need_path = f'{file}/{filename}'
    if os.path.isfile(need_path):
    	pass
    else:
	    need_data = open(need_path, 'w')
	    need_data.write(data)


print("Start the installation!")

pwd = os.getcwd()
pwl = '/home/worker/Documents'
name_service = 'NameData'
name_main = 'YourAwesomeName!'

path_service = os.path.join(pwl, name_service)
path_main = os.path.join(pwd, name_main)

os.mkdir(path_main)

try:
    os.mkdir(path_service)
    
except:
    FileExistsError

with open("source.txt") as f:
	data = f.read()

print(data)
start_the_installation(path_service, 'log.txt', '0')
start_the_installation(path_service, 'naming.txt', '')
start_the_installation(path_main, 'YourName.py', data)
