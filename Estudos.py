from datetime import datetime
import random

print('---------Olá, bem vindo a nossa empresa ---------')
nome = input('Digite seu nome: ')
idade = int(input('Digite a sua idade: '))
data_cadastro = datetime.now()
cartoes = ['R$:50,00', 'R$: 250,00', 'R$: 350,00']
cartao = random.choice(cartoes)

print(f'Olá, {nome}, seu registro foi concluido com sucesso no dia {data_cadastro.day}/{data_cadastro.month}/{data_cadastro.year}. Parabéns, houve um sorteio e você foi premiado no valor de {cartao}')
