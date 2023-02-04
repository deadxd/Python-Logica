# Exercicio resolvido por Cesar Augusto Numero 85 26/01/23
# Crie um programa onde o usuario possa digitar sete valores numéricos e cadastre-os em uma lista única que matenha separados os valores pares e impares
# No final, mostre os valores pares e impares em ordem crescente.
lista_numeros = []
lista_pares = []
lista_impares = []
for c in range(1, 8):
    numero = int(input(f'Insira o {c} valor: '))
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
lista_impares.sort()
lista_pares.sort()
lista_numeros.append(lista_pares[:])
lista_numeros.append(lista_impares[:])

print(lista_numeros)

# Metodo 2 usando lista dentro de lista
num = [[], []]

for c in range(1, 8):
    numero = int(input(f'Insira o {c} valor: '))
    if numero % 2 == 0:
        num[0].append(numero)
    else:
        num[1].append(numero)

print(num)
