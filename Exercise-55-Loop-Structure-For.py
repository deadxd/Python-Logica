# Exercicio resolvido por Cesar Augusto Numero 55 21/01/23
# Faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lidos.

peso_lista = []

for peso in range(1, 6):
    peso = float(input(f'Informe a {peso} vez o peso dos usuarios: '))
    peso_lista.append(peso)

# Metodo 1 Função Min e Max de uma lista
print(
    f'Menor peso é: {min(peso_lista)} KG \nMaior peso foi: {max(peso_lista)} Kg')

# Metodo 2 basico comparador

maior_2 = 0
menor_2 = 0

for i in range(1, 6):
    peso = float(input(f'Informe a {i} vez o peso dos usuarios: '))
    if i == 1:
        maior_2 = peso
        menor_2 = peso
    else:
        if peso > maior_2:
            maior_2 = peso
        elif peso < menor_2:
            menor_2 = peso


print(f'O maior peso é: {maior_2} e o menor peso é {menor_2}')

# Metodo 3 manipulacao de lista - Maior
maior = 0
while len(peso_lista) != 2:
    if peso_lista[-1] > peso_lista[-2]:
        maior = peso_lista[-1]
        print(peso_lista)
        peso_lista.remove(peso_lista[-2])
    else:
        print(peso_lista)
        peso_lista.remove(peso_lista[-1])
        #peso_lista[-1] = None
        maior = peso_lista[-2]

print(f'Maior número é: {maior}')
