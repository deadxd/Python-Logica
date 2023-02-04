#Exercicio Facil resolvido por Cesar Augusto Numero 98 28/01/23
    #faça um programa que tenha uma função chamada contador(), que receba 3 parametros: inicio, fim e passo e realiza a contagem.
        #seu programa tem que realizar tres contagens atraves da função criada:
            #A) de 1 ate 10, de 1 em 1
            #B) de 10 até 0, de 2 em 2
            #C) uma contagem personalizada
from time import sleep


def contador(inicio, fim, passo):
    if fim % 2 == 0:
        fim -= 1
    if fim < -1 and passo > 0:
        passo = -(passo)
    for c in range(inicio,fim,passo):
        print(c, end=' ', flush=True)
        sleep(0.3)


#Primeira contagem 1 a 10 1-1
print('Contagem de 1 até 10 de 1 em 1')
contador(1,11,1)
print()

#Segunda contagem 10 a 0 2-2
print('Contagem de 10 até 0 de 2 em 2')
contador(10,-1,-2)
print()

#Contagem personalizada
print('PERSONALIZE A CONTAGEM:')
inicio = int(input('INICIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSOS: '))

contador(inicio,fim,passo)