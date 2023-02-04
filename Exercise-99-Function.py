#Exercicio Facil resolvido por Cesar Augusto Numero 99 28/01/23
    #Faça um programa que tenha uma função chamada maior(), que receba vários parametros com valores inteiros
        #seu programa tem que analisar todos os valores e dizer qual deles é o maior.

#Metodo 1
def maior(*num):
    tupla_ordenada = sorted(num)
    print(f'O maior número analisado foi: {tupla_ordenada[-1]}')
    

maior(1,2,6,5,8,2)

#Metodo 2

def maior_2(*num):
    maior = 0
    for num_for in num:
        if num_for > maior:
            maior = num_for
    print(f'O maior número analisado foi: {maior}')

maior_2(-10,1,2,6,5,8,2,22,44,15,-2,-5)

#Metodo 3

def maior_3(*num):
    maior = max(num)
    print(f'O maior número analisado foi: {maior}')

maior_3(2,6,4,9,7,5)