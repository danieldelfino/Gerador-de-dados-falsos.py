import PySimpleGUI as sg
from faker import Faker 
import os

sg.theme('dark')

# Layout da aplicação(esqueleto)
layout = [
    [sg.Button('Gerar Nome', size=(20,0)),sg.Input(key='nome', size=(60,0))],
    [sg.Button('Gerar Profissão', size=(20,0)),sg.Input(key='profissao', size=(60,0))],
    [sg.Button('Gerar Endereço', size=(20,0)),sg.Input(key='endereco', size=(60,0))],
    [sg.Button('Gerar Placa',size=(20,0)),sg.Input(key='placa', size=(60,0))],
    [sg.Button('Gerar Cartão de Crédito',size=(20,0)),sg.Input(key='cartao_credito',size=(60,0))],
    [sg.Output(size=(85, 20))],
    [sg.Button('Imprimir Perfil Completo',size=(20,0)), sg.Button('Salvar Perfil em Arquivo', size=(20,0))],
     
]    
#Criando a janela, usando layout que foi definido
janela = sg.Window('Gerador de Dados Falsos', layout=layout)
#Lendo os eventos da tela e gerar os dados fakes
fake = Faker()
Faker.seed(0)

while True:
    event, valores = janela.Read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event  == 'Gerar Nome':
       janela['nome'].update(fake.name())
    elif event == 'Gerar Profissão':
        janela['profissao'].update(fake.job())   
    elif event == 'Gerar Endereço':
        janela['endereco'].update(fake.address()) 
    elif event == 'Gerar Placa':
        janela['placa'].update(fake.license_plate())
    elif event == 'Gerar Cartão de Crédito':
        janela['cartao_credito'].update(fake.credit_card_full())
    elif event == 'Imprimir Perfil Completo':
        print(f'NOME: {fake.name()}{os.linesep}PROFISSÃO: {fake.job()}{os.linesep}ENDEREÇO: {os.linesep}PLACA: {fake.license_plate()}')     
