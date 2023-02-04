# Exercicio resolvido por Cesar Augusto Numero 71 24/01/23
# Crie um programa que simule o funcionamento de um caixa eletronica.
# Pergunte ao usuário qual será o valor a ser sacado(int) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Considere que o caixa possui cédulas de R$ 50, R$20, R$10 e R$1.

valor_saque = int(input('Qual valor você quer sacar? R$'))

notas_50 = valor_saque // 50

resta_50 = valor_saque - (50 * notas_50)

notas_20 = resta_50 // 20

resta_20 = resta_50 - (20 * notas_20)

notas_10 = resta_20 // 10

resta_10 = resta_20 - (10 * notas_10)

notas_1 = resta_10 // 1

#resta_1 = resta_10 - (1 * notas_1)

print(f'{notas_50} Notas de R$50 \n{notas_20} Notas de R$20  \n{notas_10} Notas de R$10 \n{notas_1} Notas de R$1 ')
