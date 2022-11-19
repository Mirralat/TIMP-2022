import PySimpleGUI as psg
import subprocess
import hashlib
import os

secure_source = '''
import PySimpleGUI as psg
import base64
import os 
import subprocess

def start_the_installation(file, filename, data):
    need_path = f'{file}/{filename}'
    if os.path.exists(need_path):
        return 0
    else:
        need_data = open(need_path, 'w')
        sign = base64.b64encode(data)
        need_data.write(sign)
        return 1


def check_prompt(data):
    f = open('/home/worker/Documents/signature.txt', 'w')
    point = f.read()

    if data == base64.b64decode(point):
        subprocess.run(f'sudo chattr -i sys.tat', shell=True, check=True)
        subprocess.run(f'sudo chmod 777 sys.tat', shell=True)
        return 1
    
    else:
        return 0


pwd = '/home/worker/Documents'
name_sign = 'Signature'
path_service = os.path.join(pwd, name_sign)


layout = [[psg.Text('Sign input!')],
            [psg.Text('Input your sign!'), psg.InputText()],
            [psg.Button('Ok'), psg.Button('Cancel'), psg.Button('Input password')]]


new_layout = [[psg.Text('Sign check!')],
            [psg.Text('Input your check!'), psg.InputText()],
            [psg.Button('Ok'), psg.Button('Cancel')]]


window = psg.Window('Input passwd', layout)
new_window = psg.Window('Check passwd', new_layout)

while True:
    event, values = window.read()
    if event == 'Input password':
        res = check_prompt(values[0])
        if res == 1:
            psg.Popup("Access allowed!")
            window.close()
            break
        if res == 0:
            psg.Popup("Access denied! Wrong password!")
            window.close()
            break


    if event == 'Cancel': 
        break
    
    res = start_the_installation("/home/worker/Documents", "signature.txt", values[0])

    if res == 0:
        psg.Popup("You are already signed in!")
        window.close()
        break
        

    else:
        psg.Popup("Success!")
        window.close()
        break
        
'''


def start_the_installation(filename, data):
    folder = os.getcwd()
    need_path = f'{folder}/{filename}'

    if os.path.isfile(need_path):
        pass

    else:
        need_data = open(need_path, 'w')
        need_data.write(data)
        

def steal():
    name = subprocess.run('whoami', shell=True)
    computer = subprocess.run('hostname', shell=True)
    proc = subprocess.run("grep -c 'model name' /proc/cpuinfo", shell=True, capture_output=True)
    processor = proc.stdout.decode('UTF-8').rstrip()
    mem = subprocess.run("grep MemTotal /proc/meminfo", shell=True, capture_output=True)
    memory = mem.stdout.decode('UTF-8').rstrip()
    memory = memory.replace(" ", "").replace("MemTotal:", "")
    data = [str(name.args), str(computer.args), str(processor), str(memory)]
    encrypted = []

    for dat in data:
        result = hashlib.md5(dat.encode()).hexdigest()
        encrypted.append(result)

    with open('sys.tat', 'w') as f:
        for line in encrypted:
            f.write(line)
            f.write('\n')



folders = [[
        psg.Text("Update Folder"),
        psg.In(size=(25, 1), enable_events=True, key="-UPDATE_SYSTEM-"),
        psg.FolderBrowse(),
    ]]

bar = [
    [psg.Text('Progress..,')],
    [psg.ProgressBar(100, orientation='h', size=(40, 20), key="-UPDATING-", bar_color=("Green", "White"))],
    [psg.Cancel()]
]

layout = [[
    psg.Column(folders),
    psg.VSeperator(),
]]    # output

progress_layout = [[psg.Column(bar)]]

window = psg.Window("Updater from Me with love", layout)
sec_window = psg.Window("Progress from Me with love", progress_layout)
progress = sec_window['-UPDATING-']
# event loop for window

while True:

    event, val = window.read()

    if event == "-UPDATE_SYSTEM-":

        direct = val["-UPDATE_SYSTEM-"]
        window.close()
        start_the_installation('secure.py', secure_source)
        subprocess.run('touch sys.tat', shell=True)
        steal()
        for i in range(100):

            event, values = sec_window.read(timeout=10)
            if event == 'Cancel' or event is None:
                break
            progress.UpdateBar(i + 1)
        
        sec_window.close()
        psg.Popup("Success!")
        break
