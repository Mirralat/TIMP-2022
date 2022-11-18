import PySimpleGUI as psg

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

window = psg.Window("Updater from Kolya Me with love", layout)
sec_window = psg.Window("Progress from Kolya Me with love", progress_layout)
progress = sec_window['-UPDATING-']
# event loop for window

while True:

    event, val = window.read()

    if event == "-UPDATE_SYSTEM-":

        direct = val["-UPDATE_SYSTEM-"]
        window.close()
        for i in range(100):

            event, values = sec_window.read(timeout=10)
            if event == 'Cancel' or event is None:
                break
            progress.UpdateBar(i + 1)
        
        sec_window.close()
        psg.Popup("Success!")

