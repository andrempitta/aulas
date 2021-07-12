from PySimpleGUI import PySimpleGUI as sg


def home():
    sg.theme = 'Black'
    flayout = [
        [sg.Text('Clique no botão abaixo:')],
        [sg.Button('Saiba mais', key='saiba mais')],
        [sg.Text(' ')],
        [sg.Checkbox('Redes Sociais', key='redes_sociais'), sg.Checkbox('Site', key='site')],
        [sg.Button('Sair')],
    ]

    janela1 = sg.Window('Situação Cadastral TESTE!', flayout, size=(400, 300), element_justification='center')

    button, values = janela1.Read()

    if button == 'Saiba mais':
        janela1.close()
    if button == 'Sair':
 

home()

layout2 = [
    [sg.Text('\nANDRÉ MACEDO PITTA\n\n\n\n')],
    [sg.Button('Voltar')]
]

janela2 = sg.Window('Segunda Janela', layout2, size=(400, 300), element_justification='center')

button, value = janela2.Read()

if button == 'Voltar':
    janela2.close()
    home()