from PySimpleGUI import PySimpleGUI as sg 

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario:'), sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha:  '), sg.Input(key='senha', size=(20,1),password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
# Janela
janela = sg.Window('Tela de login', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'augusto' and valores['senha'] == '123456':
            print('Olá, seja bem vindo!')
