import PySimpleGUI as sg

def login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')],
    ]
    return sg.Window('Login', layout=layout, finalize=True)

def janela_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer pedido')],
        [sg.Checkbox('Pizza Calabreza', key='pizza1'), sg.Checkbox('Pizza Mussarela', key='pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]
    ]
    return sg.Window('Pedido', layout=layout, finalize=True)


janela1, janela2 = login(), None

while True:
    window, event, value = sg.read_all_windows()
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and event == sg.WINDOW_CLOSED:
        break
    if window == janela2 and event == 'Voltar':
        janela2.hide()        
        janela1.un_hide()
    if window == janela2 and event == 'Fazer Pedido':
        if value['pizza1'] == True and value['pizza2'] == True:
            sg.popup('Foi solicitado uma pizza de Calabreza e outra de Muzzarela!', title='Pedido')
        elif value['pizza1'] == True and value['pizza2'] == False:
            sg.popup('Foi solicitado uma pizza de Calabreza!', title='Pedido')
        elif value['pizza1'] == False and value['pizza2'] == True:
            sg.popup('Foi solicitado uma pizza de Muzzarela!', title='Pedido')
            