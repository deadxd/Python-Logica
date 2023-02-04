# Exercicio resolvido por Cesar Augusto Numero 9 16/01/23
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

numero_inteiro = int(input('Informe um numero inteiro qualquer: '))
tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'{"=" :=>20}')
print(f'A tabuada do {numero_inteiro} é: ')
for i in range(0, 10):
    print(f'{numero_inteiro} X {tabuada[i]} = {numero_inteiro *tabuada[i]}')

print(f'{"=" :=>20}')
