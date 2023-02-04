# Exercicio resolvido por Cesar Augusto Numero 16 18/01/23
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# EX Insira Um Numero: 6.127
# Result: O número 6.127 tem a parte inteira de 6
import math

numero = float(input('INSIRA UM NÚMERO REAL: '))

numero_inteiro_floor = math.floor(numero)

numero_inteiro_trunc = math.floor(numero)

numero_inteiro_int = int(numero)

print(f'O número {numero} tem a parte inteira de {numero_inteiro_floor} ou {numero_inteiro_trunc} ou {numero_inteiro_int}')
