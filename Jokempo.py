from time import sleep
from random import  randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é sua jogada?:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format( itens[jogador]))
print('-=' * 11)

#Computador jogou pedra

if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Ganhou')
    elif jogador == 2:
        print('Jogador perdeu')
    else:
        print('Jogada invalida!')

#Computador jogou papel

elif computador == 1:
    if jogador == 0:
        print('Jogador perdeu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Ganhou')
    else:
        print('Jogada invalida')

#Computador jogou tesoura

elif computador == 2:
    if jogador == 0:
        print('Jogador Ganhou')
    elif jogador == 1:
        print('jogador perdeu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada invalida')
