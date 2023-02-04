# Exercicio resolvido por Cesar Augusto Numero 30 19/01/23
# Crie um programa que leia um numéro inteiro e mostre na tela se é par ou impar

numero = int(input('Informe um número inteiro para tratamento: '))
numero_divisao = numero % 2
print(f'O Número {numero} é Impar' if numero_divisao ==
      1 else f'O Número {numero} é Par')
