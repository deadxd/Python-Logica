# Exercicio resolvido por Cesar Augusto Numero 86 26/01/23
# Crie um programa que crie uma matriz de dimensões 3x3 e preencha tudo com valores lidos pelo teclado
# No final me mostre a matriz na tela.

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

# Metodo 2

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um valor : '))

print(matriz)
