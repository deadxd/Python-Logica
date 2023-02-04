# Exercicio resolvido por Cesar Augusto Numero 87 26/01/23
# Aprimore o exercicio 86, mostrando:
# A) A soma de todos os valores pares
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha

matriz_principal = []
matriz_referencia = []
for c in range(1, 10):
    valor = int(input(f'Insira o {c} valor: '))
    matriz_referencia.append(valor)
    if c == 3:
        matriz_principal.append(matriz_referencia[:])
        matriz_referencia.clear()
    elif c == 6:
        matriz_principal.append(matriz_referencia[:])
        matriz_referencia.clear()
    elif c == 9:
        matriz_principal.append(matriz_referencia[:])
        matriz_referencia.clear()

for each in matriz_principal:
    print(each)

# Soma de todos os valores pares
soma_pares = 0
count = 0
for c in range(0, len(matriz_principal[1])):
    count = 0
    while True:
        print(matriz_principal[c][count])
        if matriz_principal[c][count] % 2 == 0:
            soma_pares += matriz_principal[c][count]
        count += 1
        if count == len(matriz_principal):
            break
print(f'A soma de todos pares é: {soma_pares}')
# A soma dos valores da terceira coluna
soma = 0
for c in range(0, len(matriz_principal[1])):
    soma += matriz_principal[c][2]
print(f'A soma da Terceira coluna é: {soma}')

# O maior valor da segunda linha
maior = 0
for c in range(0, len(matriz_principal[1])):
    if maior < matriz_principal[1][c]:
        maior = matriz_principal[1][c]
print(f'O maior valor da segunda linha é: {maior}')
