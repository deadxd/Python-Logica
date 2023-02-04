# Exercicio resolvido por Cesar Augusto Numero 51 21/01/23
# Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritimetrica. no final, mostre os 10 primeiro termos dessa progressão.

termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão do termo: '))

# Metodo 1 usando formula da PA
decimo = termo + (10 - 1) * razao

for i in range(termo, decimo + 1, razao):
    print(i)

# Metodo 2
for i in range(0, 10):
    print(termo)
    termo += razao
