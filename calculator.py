import PySimpleGUI as sg
import string

def create_window (theme):
    sg.theme(theme)
    sg.set_options(font = 'Calibri 20', button_element_size = (2, 1))
    button_size = (4, 1)
    special_size = (6, 1)
    menu_options = ['', ['LightGray1', 'DarkGray8', 'dark', 'random']]

    layout = [
        [sg.Text('0', font = 'Calibri 35', justification = 'right', expand_x = True, pad = (10, 10), key= '-OUTPUT-')],
        [sg.Button('Clear', size = special_size, key= '-CLEAR-'), sg.Button('OFF', size = special_size, key= '-OFF-'), sg.ButtonMenu('Theme', menu_options , size = special_size, key= '-THEME-', expand_y= True)],
        [sg.Button('%', size = special_size), sg.Button('**', size = special_size), sg.Button('/', size = special_size)],
        [sg.Button(7, size = button_size), sg.Button(8, size = button_size), sg.Button(9, size = button_size), sg.Button('*', expand_x= True)],
        [sg.Button(4, size = button_size), sg.Button(5, size = button_size), sg.Button(6, size = button_size), sg.Button('+', expand_x= True)],
        [sg.Button(1, size = button_size), sg.Button(2, size = button_size), sg.Button(3, size = button_size), sg.Button('-', expand_x= True)],
        [sg.Button(0, size = button_size), sg.Button('.', size = button_size), sg.Button('=', expand_x= True)]
    ]

    return sg.Window('Calculator', layout)

numbers = list(string.digits)
numbers.append('.')
operators = ['%', '**', '/', '*', '+', '-']
current_number = ['0']
operation = []

theme_mode = ['Theme', ['LightGray1', 'DarkGray8', 'dark', 'random']]
window = create_window('LightGray1')

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == '-OFF-':
        break

    if event == '-THEME-':
        window.close()
        window = window = create_window(values['-THEME-'])

    if event in numbers:
        if '0' in current_number:
            current_number.remove('0')
        current_number.append(event)
        num_string = ''.join(current_number)
        window['-OUTPUT-'].update(num_string)

    if event in operators:
        operation.append(''.join(current_number))
        current_number.clear()
        operation.append(event)
        window['-OUTPUT-'].update(event)

    if event in '=':
        operation.append(''.join(current_number))
        if operation[-1] != '0':
            current_number.append(str(eval(''.join(operation))))
            window['-OUTPUT-'].update(current_number[-1])
            operation.clear()
            operation.append(current_number[-1])
            current_number.clear()
        else:
            window['-OUTPUT-'].update('Division por 0')
            operation.clear()
            current_number.clear()

    if event == '-CLEAR-':
        window['-OUTPUT-'].update('0')
        current_number.clear()
        current_number.append('0')
        operation.clear()

window.close()