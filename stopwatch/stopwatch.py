import PySimpleGUI as sg

from time import time

def create_window():

    sg.theme('DarkBlack')

    button_size = (4, 1)

    sg.set_options(

        font=('Young 50'),

        button_element_size=button_size

    )

    layout = [

        [sg.Push(), sg.Image('./cross.png', pad=(5, 10), enable_events=True, key='-CLOSE-')],
        
        [sg.VPush()],
        
        [sg.Text('', key='-TIME-')],
        
        [

            sg.Button('Start', button_color=('#FFFFFF', '#FF0000'), border_width=0, size=button_size, key='-STARTSTOP-'),
            
            sg.Button('Lap', button_color=('#FFFFFF', '#FF0000'), border_width=0, size=button_size, key='-LAP-', visible=False)
       
        ],
        
        [sg.Column([[]], key = '-LAPS-')],
        
        [sg.VPush()]
    
    ]
    return sg.Window(

        'Stopwatch',

        layout,

        size=(500, 500),

        no_titlebar=True,

        element_justification='center'

    )

window = create_window()

start_time = 0

active = False

lap_amount = 1

while True:

    event, values = window.read(timeout=10)

    if event in (sg.WIN_CLOSED, '-CLOSE-'):

        break

    if event == '-STARTSTOP-':

        if active:

            # Stop the stopwatch

            active = False

            window['-STARTSTOP-'].update('Reset')

            window['-LAP-'].update(visible=False)

        else:

            if start_time > 0:

                window.close()

                window = create_window()

                start_time = 0

                lap_amount = 1

            else:

                start_time = time()

                active = True

                window['-STARTSTOP-'].update('Stop')

                window['-LAP-'].update(visible=True)

    if active:

        elapsed_time = round(time() - start_time, 1)

        window['-TIME-'].update(elapsed_time)

    if event == '-LAP-':

        if lap_amount <= 3:

            window.extend_layout(window['-LAPS-'], [[sg.Text(lap_amount), sg.VSeparator(), sg.Text(elapsed_time)]])
        
            lap_amount += 1

window.close()
