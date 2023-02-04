#Exercicio Facil resolvido por Cesar Augusto Numero 100 28/01/23
    #Faça um programa que tenha uma lista chamada números e duas funções chamda sorteio() e somaPar()
        #A primeira função vai sortear 5 números e vai coloca-los dentro da lista
        #A segunda função vai mostra a soma entre todos os valores PARES sorteados pela função anterior.

from random import randint

def sorteio(lista):
    for num in range(5):
        sorteado = randint(1, 10)
        lista.append(sorteado)
    print(numeros)

def somaPAR(lista):
    soma = 0
    #sorteado = sorteio()
    for each in lista:
        if each % 2 == 0:
            soma += each
    print(f'A soma entre todos os pares sorteados foram: {soma}')


numeros = []
sorteio(numeros)
somaPAR(numeros)