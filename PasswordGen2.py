import random
import PySimpleGUI as sg

class PassGen:
    def __init__(self):
        sg.theme('Black')
        layout = [
            [sg.Text('Site//Software', size=(15, 1)),
            sg.Input(key='site', size=(20, 1))],
            [sg.Text('Email//Username', size=(15, 1)), 
            sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Password Length', size=(15, 1)),
            sg.Combo(values=list(range(31)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(37, 5))],
            [sg.Button('Generate Password')],
        ]
        self.janela = sg.Window('Password Generator', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Generate Password':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)

    def gerar_senha(self, valores):
        chars_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV!@#$%¨¨&*'
        chars = random.choices(chars_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a') as arquivo:
            arquivo.write(f"site: {valores['site']}, usuario: {valores['usuario']}, nova senha: {nova_senha}\n")
        print('Password Saved!')


gen = PassGen()
gen.Iniciar()
