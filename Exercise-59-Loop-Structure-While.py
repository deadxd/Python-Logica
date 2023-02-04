# Exercicio resolvido por Cesar Augusto Numero 59 23/01/23
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1]somar [2]multiplicar [3]maior [4]novos números [5]sair do programa
from time import sleep

menu = 0
numero_1 = int(input('Informe o primeiro valor: '))
numero_2 = int(input('Informe o segundo valor: '))

while menu != 5:
    sleep(1)
    menu = int(input(
        '[1]Somar \n[2]multiplicar \n[3]maior \n[4]Insirer novos Números \n[5]sair\nInforme o que deseja fazer: '))

    if menu == 1:
        somar = numero_1 + numero_2
        print(f'A Soma de {numero_1} + {numero_2} é: {somar}')

    elif menu == 2:
        multiplicar = numero_1 * numero_2
        print(
            f'A Multiplicação de {numero_1} x {numero_2} é: {multiplicar}')

    elif menu == 3:
        if numero_1 > numero_2:
            print(f' O {numero_1} e maior que {numero_2}')
        else:
            print(f' O {numero_2} e maior que {numero_1}')
    elif menu == 4:
        numero_1 = int(input('Informe o novo valor de primeiro valor: '))
        numero_2 = int(input('Informe o novo valor de segundo valor: '))
    elif menu == 5:
        sleep(1)
        print('Fim do programa')
