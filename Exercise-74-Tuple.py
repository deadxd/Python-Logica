# Exercicio resolvido por Cesar Augusto Numero 74 24/01/23
# Crie um programa que vai gerar cinco números aleatorio e colocar em uma tupla.
# Mostre a listagem de números gerados e tamém indique o menor e o maior valor que estão na tupla.

from random import randint

numero_aleatorio = ()

for i in range(0, 5):
    numero_aleatorio += (randint(0, 9),)

menor_numero = min(numero_aleatorio)
maior_numero = max(numero_aleatorio)

print(
    f'Os Números Gerados foram: {numero_aleatorio} O maior é: {maior_numero} e o menor é: {menor_numero}')
