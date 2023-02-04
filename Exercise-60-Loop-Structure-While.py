# Exercicio resolvido por Cesar Augusto Numero 60 23/01/23
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120

from math import factorial

numero = int(input('Informe o valor para saber seu fatorial: '))
contador = 1
numero_fixo = numero

# Metodo 1 While

while numero != 0:
    numero -= 1
    if numero != 0:

        contador += contador * numero
        print(contador)

print(f'O fatorial de {numero_fixo} é: {contador}')

# Metodo 2 Função factorial

fatorial = factorial(numero_fixo)
print(f'O fatorial de {numero_fixo} é: {fatorial}')

# Metodo 3 While

print(f'Calculando {numero_fixo}! = ', end='')
c = numero_fixo
f = 1
while c > 0:
    print(f' {c}', end=' ')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f' {f}', end='')
