import random
import PySimpleGUI as sg
import os
from playsound import playsound


class PassGen:
    def __init__(self):
        sg.theme("DarkGrey3")
        playsound('relax.mp3', block=False)
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),
             sg.Input(key='site', size=(20, 1))],
            [sg.Checkbox('Caracteres Especiais', default=False, key='caracteres_especiais')],
            [sg.Text('Email/Usuário', size=(10, 1)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de Caracteres', ),
             sg.Combo(values=list(range(30)), key='total', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]
        ]

        self.janela = sg.Window('Gerador de Senhas', layout)

    def iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WIN_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)

    def gerar_senha(self, valores):
        letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
        caracteres_especiais = '!@#$%&*'

        if valores['caracteres_especiais']:
            total = letras + caracteres_especiais
            chars = random.choices(total, k=int(valores['total']))
        else:
            chars = random.choices(letras, k=int(valores['total']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"site: {valores['site']}, usuário: {valores['usuario']}, nova senha: {nova_senha}\n")

        print('Arquivo com senha gerado!')


gen = PassGen()
gen.iniciar()
