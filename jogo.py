from random import choice
from time import sleep
jogo = ['PEDRA', 'PAPEL', 'TESOURA']
maquina = choice(jogo)
player = str(input('''Pedra, Papel ou Tesoura?
 ''')).upper()
sleep(1)
print('Pedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesoura!!!')
sleep(1)
print('-'*20)
print('   Maquina > ', maquina)
print('   Você > ', player)
print('-'*20)
sleep(2)
if player == maquina:
    print('   EMPATE!')
elif player == 'PEDRA':
    if maquina == 'TESOURA':
        print('   Você Venceu!')
    elif maquina == 'PAPEL':
        print('   Maquina Venceu!')
elif player == 'TESOURA':
    if maquina == 'PAPEL':
        print('   Você Venceu!')
    elif maquina == 'PEDRA':
        print('   Maquina Venceu!')
elif player == 'PAPEL':
    if maquina == 'PEDRA':
        print('   Você Venceu!')
    elif maquina == 'TESOURA':
        print('   Maquina Venceu!')
print('-'*20)
# seja carainhoso com o codigo
