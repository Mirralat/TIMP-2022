import PySimpleGUI as psg
import base64
import os 
import subprocess

def start_the_installation(file, filename, data):
    need_path = f'{file}/{filename}'
    if os.path.exists(need_path):
        return 0
    else:
        ut = data.encode('UTF-8')
        need_data = open(need_path, 'w')
        sign = base64.b64encode(ut)
        need_data.write(str(sign))
        return 1


def check_prompt(data):
    f = open('/home/worker/Documents/signature.txt', 'r')
    point = f.read()
    data = data.encode('UTF-8')
    sign = str(base64.b64encode(data))
    if sign == point:
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
    
    res = start_the_installation("/home/worker/Documents", "signature.txt", str(values[0]))

    if res == 0:
        psg.Popup("You are already signed in!")
        window.close()
        break
        

    else:
        psg.Popup("Success!")
        window.close()
        break
        
