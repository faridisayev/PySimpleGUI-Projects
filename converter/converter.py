"""

    An event is triggered by a certain action.
    Every element can trigger an event.
    A button triggers another event.
    The name of event will be the key of the button.

    There are several elements that can contain values, like Input.
    These values are stored in one dictionary, called values.
    You can access that one with the name of the input element.

    Every element has an update method.
    It can be used to change text, visibility etc.

"""

import PySimpleGUI as sg

sg.theme('DarkBlue')

sg.set_options(
    font = ('Young 30')
)

# create a window 

layout = [

    [
        sg.Input('', key = '-INPUT-'),

        sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key = '-UNITS-'),

        sg.Button('Convert', key = '-CONVERT-')    
    ],

    [sg.Text('Output', key = '-OUTPUT-')]

]
 
window = sg.Window('Converter', layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:

        # break from infinite loop 

        break

    if event == '-CONVERT-':

        input_value = values['-INPUT-']

        try:

            input_value = float(input_value)

            match values['-UNITS-']:

                case 'km to mile':

                    output = round(float(input_value) * 0.6214, 2)

                    output_string = f'{input_value} km are {output} miles.'

                case 'kg to pound':

                    output = round(float(input_value) * 2.20462, 2)

                    output_string = f'{input_value} kg are {output} pounds.'

                case 'sec to min':

                    output = round(float(input_value) / 60, 2)

                    output_string = f'{input_value} seconds are {output} minutes.'

            window['-OUTPUT-'].update(output_string)

        except ValueError:

            window['-OUTPUT-'].update('Please enter numeric value.')

        except:

            window['-OUTPUT-'].update('Unknown error occured.')


# close the window 

window.close()
