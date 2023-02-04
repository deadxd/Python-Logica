# Exercicio resolvido por Cesar Augusto Numero 45 20/01/23
# Crie um programa que faça o computador jogar jokenpô com você.

from time import sleep
from random import choice

jokenpo = ['pedra', 'papel', 'tesoura']

minha_escolha = str(input(
    'Informe sua escolha: \nInsira [Pedra}\nInsira [Papel]\nInsira [Tesoura]\n')).strip().lower()

if minha_escolha == 'pedra' or minha_escolha == 'papel' or minha_escolha == 'tesoura':
    computador_escolha = choice(jokenpo)

    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO')
    sleep(0.5)

    print(
        f'Você escolheu: {minha_escolha} e o Computador escolheu: {computador_escolha}')
    sleep(1)

    if minha_escolha == computador_escolha:
        print(f'EMPATAMOS')
    elif minha_escolha == 'pedra' and computador_escolha == 'papel':
        print(f'O computador venceu!')
    elif minha_escolha == 'pedra' and computador_escolha == 'tesoura':
        print(f'O Jogador venceu!')
    elif minha_escolha == 'papel' and computador_escolha == 'tesoura':
        print(f'O Computador venceu!')
    elif minha_escolha == 'papel' and computador_escolha == 'pedra':
        print(f'O Jogador venceu!')
    elif minha_escolha == 'tesoura' and computador_escolha == 'pedra':
        print(f'O Computador venceu!')
    elif minha_escolha == 'tesoura' and computador_escolha == 'papel':
        print(f'O Jogador venceu!')
else:
    print('Escolha uma opção valida')
