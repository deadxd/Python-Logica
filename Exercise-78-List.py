# Exercicio resolvido por Cesar Augusto Numero 78 25/01/23
# Faça um programa que leia 5 valores numéricos e guarde em uma lista
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
numeros = []
count = 0
for valor in range(0, 5):
    numeros.append(int(input(f'Informe um valor na posição {count}: ')))
    count += 1

print(
    f'A lista formada é: {numeros} \nO maior valor é: {max(numeros)} \nO menor valor é: {min(numeros)}')
